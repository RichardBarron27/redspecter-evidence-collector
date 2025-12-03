# 🔒 Red Specter Evidence Collector (MVP)

> The pentester's evidence ledger — from chaos to case file.

A simple CLI tool to structure, timestamp, and store pentest evidence as you work.

## Quickstart

```bash
# Initialize a new project
python3 evid/cli.py init --project "Lab-Test"

# Collect command output as evidence
python3 evid/cli.py collect command \
  --project "Lab-Test" \
  --cmd "whoami" \
  --target "10.10.10.5" \
  --tags "initial-access"
---

### 🔗 Explore the Red Specter tool suite

- 🗺 **ScriptMap** – Map, group, and document your security/automation scripts in seconds.  
  https://github.com/RichardBarron27/redspecter-scriptmap

- 🧨 **Red Specter Offensive Framework** – Modular bash framework for recon, web enum, vuln scanning, and more (Kali-friendly).  
  https://github.com/RichardBarron27/red-specter-offensive-framework

- 📧 **Red Specter Email OSINT** – Email-focused OSINT helper for investigators and defenders.  
  https://github.com/RichardBarron27/redspecter-emailosint
