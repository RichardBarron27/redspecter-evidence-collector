"""
AI Shield - Comprehensive AI Security Framework
Copyright (c) 2025-2026 Red Specter Security Research Ltd
All rights reserved. Proprietary and confidential.
"""

import argparse
from pathlib import Path
from datetime import datetime, date
import csv
import shlex
import subprocess

BASE_DIR_NAME = "evidence"

def get_base_dir():
    # Evidence folder will live under the current working directory
    return Path.cwd() / BASE_DIR_NAME

def init_project(project_name: str):
    base = get_base_dir()
    project_dir = base / project_name
    project_dir.mkdir(parents=True, exist_ok=True)
    print(f"[+] Project directory created or already exists: {project_dir}")

    # make sure a timeline file exists
    timeline_path = project_dir / "timeline.csv"
    if not timeline_path.exists():
        with timeline_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "project", "target", "type", "file_path", "tags", "details"])
        print(f"[+] Created timeline: {timeline_path}")
    else:
        print(f"[i] Timeline already exists: {timeline_path}")

def sanitize_filename(s: str, max_len: int = 40) -> str:
    # Turn a command into a safe filename (no spaces, slashes, etc.)
    safe = "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in s.strip())
    if len(safe) > max_len:
        safe = safe[:max_len]
    return safe or "command"

def collect_command(project: str, cmd: str, target: str = "unknown", tags: str = "", dry_run: bool = False):
    if not project:
        raise SystemExit("[-] --project is required for collect command")

    base = get_base_dir()
    project_dir = base / project
    if not project_dir.exists():
        raise SystemExit(f"[-] Project directory does not exist: {project_dir}. Run 'evid init --project \"{project}\"' first.")

    today = date.today().isoformat()  # YYYY-MM-DD
    timestamp = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    safe_cmd = sanitize_filename(cmd)

    target_dir = project_dir / today / target / "command"
    target_dir.mkdir(parents=True, exist_ok=True)

    out_file = target_dir / f"{safe_cmd}-{timestamp}.txt"

    if dry_run:
        print(f"[DRY-RUN] Would save command output to: {out_file}")
        return

    # Actually run the command
    print(f"[+] Running command: {cmd}")
    try:
        # Use shlex.split for cross-platform command parsing (no shell=True)
        cmd_list = shlex.split(cmd)
        result = subprocess.run(cmd_list, capture_output=True, text=True)
    except Exception as e:
        raise SystemExit(f"[-] Failed to run command: {e}")

    content = []
    content.append(f"# evid command collector")
    content.append(f"# timestamp: {timestamp}")
    content.append(f"# project: {project}")
    content.append(f"# target: {target}")
    content.append(f"# cmd: {cmd}")
    content.append("")
    content.append("## stdout")
    content.append(result.stdout or "(no stdout)")
    content.append("")
    content.append("## stderr")
    content.append(result.stderr or "(no stderr)")
    content.append("")
    content.append(f"## return code: {result.returncode}")

    with out_file.open("w", encoding="utf-8") as f:
        f.write("\n".join(content))

    print(f"[+] Saved evidence to: {out_file}")

    # Append to timeline
    timeline_path = project_dir / "timeline.csv"
    if not timeline_path.exists():
        # create header if missing
        with timeline_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "project", "target", "type", "file_path", "tags", "details"])

    rel_path = out_file.relative_to(project_dir)
    with timeline_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, project, target, "command", str(rel_path), tags, cmd])

    print(f"[+] Updated timeline: {timeline_path}")

def main():
    parser = argparse.ArgumentParser(
        prog="evid",
        description="Red Specter Evidence Collector (MVP) - collect and organize pentest evidence."
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # evid init --project "Name"
    p_init = subparsers.add_parser("init", help="Initialize a new evidence project")
    p_init.add_argument("--project", required=True, help="Project name, e.g. 'Acme-External-2025'")

    # evid collect ...
    p_collect = subparsers.add_parser("collect", help="Collect evidence")

    # nested subcommands under 'collect'
    collect_sub = p_collect.add_subparsers(dest="collect_type", required=True)

    # evid collect command ...
    p_cmd = collect_sub.add_parser("command", help="Collect command output as evidence")
    p_cmd.add_argument("--project", required=True, help="Project name (must already exist)")
    p_cmd.add_argument("--cmd", required=True, help="Command to run, e.g. 'whoami'")
    p_cmd.add_argument("--target", default="unknown", help="Target IP/hostname/context label")
    p_cmd.add_argument("--tags", default="", help="Comma-separated tags, e.g. 'initial-access,linux'")
    p_cmd.add_argument("--dry-run", action="store_true", help="Don't run, just show where output would go")

    args = parser.parse_args()

    if args.subcommand == "init":
        init_project(args.project)
    elif args.subcommand == "collect" and args.collect_type == "command":
        collect_command(
            project=args.project,
            cmd=args.cmd,
            target=args.target,
            tags=args.tags,
            dry_run=args.dry_run,
        )
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
