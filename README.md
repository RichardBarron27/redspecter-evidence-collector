# 🔒 Red Specter Evidence Collector (MVP)

> **The pentester's evidence ledger — from chaos to case file.**  
> Turn chaotic output into clean, timestamped, professional case evidence.
---


## ⭐ What It Does

- Automatically organizes pentest evidence
- Timestamped + tagged + stored by:
  - Project
  - Date
  - Target
  - Evidence type
- Maintains a master `timeline.csv`
- Works with any CLI tool
- Keeps all evidence **local** (good OPSEC)
---


## 🚀 Quickstart

```bash
# Initialize a new engagement
python3 evid/cli.py init --project "Lab-Test"

# Collect command output as evidence
python3 evid/cli.py collect command \
  --project "Lab-Test" \
  --cmd "whoami" \
  --target "10.10.10.5" \
  --tags "initial-access"
evidence/
└── Lab-Test
    ├── YYYY-MM-DD
    │   └── <target>
    │       └── command/
    │           └── <cmd>-<timestamp>.txt
    └── timeline.csv

---

### Step 4 — Why This Matters

```md
---


## 🧩 Why This Matters

Pentesters often end up with:

- Random terminal outputs  
- Screenshots everywhere  
- Notes scattered around  


📌 This tool solves that with **automated case organization**.

Use it for:
- Pentests
- Red team ops
- CTFs
- Incident response
---


## 🛣️ Roadmap

| Feature | Status |
|--------|:-----:|
| Command output collector | ✅ MVP |
| Screenshot collector | 🔜 |
| `--from-stdin` support (pipe tool output) | 🔜 |
| Clipboard capture | 🔜 |
| Local timeline web viewer (`evid serve`) | 🔜 |
| PDF/HTML report export | 🔜 |
| Hash + sign for chain-of-custody | 🔜 |
---


## 📦 Requirements

- Python 3.8+

(More installation methods coming soon)
---


## 🔗 Red Specter Offensive Suite

Part of the **Red Specter** ethical cybersecurity ecosystem:

| Tool | Purpose | Link |
|------|---------|------|
| 🧨 Offensive Framework | Modular recon→web enum→vuln scanning workflow | https://github.com/RichardBarron27/red-specter-offensive-framework |
| 🗺 ScriptMap | Auto-discover and organize your scripts intelligently | https://github.com/RichardBarron27/redspecter-scriptmap |
| 📧 Email OSINT | Lightweight investigator-friendly email intel tool | https://github.com/RichardBarron27/redspecter-emailosint |
| 🔒 Evidence Collector | Structured storage & timeline of pentest findings | https://github.com/RichardBarron27/redspecter-evidence-collector |
---


## 🧑‍💻 Author

**Richard Barron – Red Specter Founder**  
AI Partner: **Vigil**

⭐ If this tool helps you — please consider giving it a star!



