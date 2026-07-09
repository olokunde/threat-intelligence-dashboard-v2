# Threat Intelligence Dashboard V2

A Python command-line tool for tracking threat indicators (IPs and domains) with
automatic severity classification, persistent SQLite storage, search, and JSON reporting.

## Why I built this

I'm a security-minded IT professional building a portfolio of practical security
tooling. V1 of this project stored threats in CSV files; I rebuilt it around SQLite
to learn database-backed persistence — the same pattern real threat-tracking
systems use — and added search and reporting on top.

## Features

- Add threat indicators with a 1–100 threat score
- Automatic severity classification (Critical / High / Medium / Low)
- Persistent storage in SQLite — records survive between sessions
- Substring search across stored indicators
- Dashboard summary (total, critical, and high counts)
- One-command JSON report export for sharing findings

## Threat classification

| Score  | Level    |
|--------|----------|
| 80–100 | Critical |
| 60–79  | High     |
| 40–59  | Medium   |
| 1–39   | Low      |

## Tech stack

- Python 3 (standard library only — no dependencies to install)
- SQLite (via `sqlite3`)
- JSON (via `json`)

## How to run

```bash
python threat_intel_v2.py
```

You'll get an interactive menu:

```text
Threat Intelligence Dashboard V2

1. Add Threat
2. View Threats
3. Search Threat
4. Dashboard Summary
5. Export JSON Report
6. Exit
```

## Example output

[screenshot here]

Sample of the exported `threat_report.json`:

```json
[
    {
        "indicator": "8.8.8.8",
        "type": "IP",
        "score": 95,
        "level": "Critical"
    }
]
```

## What I'd improve next

- Input validation: reject non-numeric or out-of-range scores instead of crashing
- Enrich indicators automatically via the AbuseIPDB or VirusTotal API
- A small Flask web dashboard on top of the same database