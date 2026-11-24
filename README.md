# Alien Field Notes — The Two-Day Earth Review

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![make.fun](https://img.shields.io/badge/make.fun-bounty-green.svg)

An alien tourist's one-line review of planet Earth, written for the
[make.fun bounty](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000).

## What it does

`main.py` writes exactly one original line of plain text (max 200
characters) to `/output/entry.txt` — no trailing newline. The line is a
review of Earth by an alien tourist, then read back and verified
byte-for-byte before the program reports its SHA-256.

## Run it

```bash
python3 main.py
```

Output: `/output/entry.txt` — 182 characters, 184 bytes UTF-8.

## License

MIT — see [LICENSE](LICENSE).

---
Built for the make.fun bounty — ref=bbbzard3
