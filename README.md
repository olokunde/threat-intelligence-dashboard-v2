# Threat Intelligence Dashboard V2

## Overview

Threat Intelligence Dashboard V2 is a Python-based cybersecurity intelligence platform that stores, searches, analyzes, and reports threat indicators using a SQLite database.

Unlike the previous version that relied on CSV files, this version uses persistent database storage and supports advanced search and reporting capabilities.

---

## Features

- Add threat indicators
- Threat scoring system
- Automatic threat classification
- SQLite database storage
- Search indicators
- Dashboard summaries
- JSON report export
- Persistent threat records

---

## Technologies Used

- Python
- SQLite3
- JSON
- Cybersecurity Analytics
- Threat Intelligence

---

## Threat Levels

| Score | Level |
|---------|---------|
| 80-100 | Critical |
| 60-79 | High |
| 40-59 | Medium |
| 1-39 | Low |

---

## Project Structure

```text
threat-intelligence-dashboard-v2/

├── threat_intel_v2.py
├── threat_intel.db
├── threat_report.json
└── README.md
```

---

## Example Menu

```text
Threat Intelligence Dashboard V2

1. Add Threat
2. View Threats
3. Search Threat
4. Dashboard Summary
5. Export JSON Report
6. Exit
```

---

## Example Use Case

Security analysts can track suspicious:

- IP Addresses
- Domains
- Indicators of Compromise (IOCs)

The application assigns threat levels and stores findings for future analysis.

---

## Skills Demonstrated

- Python Development
- SQLite Databases
- JSON Processing
- Cybersecurity Analytics
- Threat Intelligence
- Data Persistence
- Security Reporting

---

## How to Run

```bash
python threat_intel_v2.py
```

---

## Future Improvements

- Threat Intelligence API integration
- VirusTotal integration
- AbuseIPDB integration
- Web dashboard with Flask
- User authentication
- Risk trend visualization
- Threat correlation engine

---

## Future Features

- CSV Export
- Dark Mode
- PDF Export

## Author

Olaoluwa Olokunde
