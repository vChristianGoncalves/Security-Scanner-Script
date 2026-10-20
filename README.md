# 🛡️ Python Security & Header Scanner

> ⚠️ **PROJECT UNDER CONSTRUCTION / WORK IN PROGRESS**  
> This repository is currently under active development. New features, code optimizations, and improved exception handling are being added regularly.

---

## 📌 General Overview

**Python Security & Header Scanner** is a command-line tool developed in Python 3 designed for automating basic network and web application security audits. 

The project aims to provide a lightweight script (without heavy external dependencies) that allows students and cybersecurity analysts to perform:
1. **TCP Port Scanning:** Identification of exposed services and open ports on a target host using sockets.
2. **HTTP Header Audit:** Verification of key security headers based on **OWASP** recommendations (*Strict-Transport-Security*, *Content-Security-Policy*, *X-Frame-Options*, etc.).

---

## 🚀 Current Project Status

The tool currently features a functional **Minimum Viable Product (MVP)** that handles the following tasks:
- [x] Domain name resolution (DNS to IP).
- [x] Synchronous multi-port scanning using `socket`.
- [x] Inspection of HTTP/HTTPS responses and OWASP header evaluation.
- [ ] *In Progress:* Implementation of concurrent/asynchronous scanning (`threading` or `asyncio`) to improve speed.
- [ ] *In Progress:* Exporting results to structured formats (`JSON` / `CSV`).
- [ ] *Pending:* Basic service banner detection module (*Banner Grabbing*).

---

## 🛠️ Technologies & Libraries Used

- **Language:** Python 3.x
- **Native Modules:**
  - `socket`: Low-level network connection management.
  - `urllib.request`: HTTP request handling and header inspection.
  - `datetime` / `sys`: Execution control and timestamps.

---
