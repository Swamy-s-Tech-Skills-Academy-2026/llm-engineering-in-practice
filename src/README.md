# `src/` — simple week / day layout

Learning code is organized **by week and day**. Only create subfolders when that day needs them.

```text
src/
├── README.md
├── setup/                    ← shared diagnostics (exception: not week/day scoped)
│   ├── run_diagnostics.py
│   ├── 01_diagnostics.py
│   ├── 02_diagnostics.ipynb
│   └── 03_troubleshooting.ipynb
└── week1/
    └── day1/                 ← current focus: Week 1, Day 1 only
        ├── README.md
        ├── day1.ipynb
        ├── scraper.py
        └── eval/             ← created because Day 1 uses experiment logging
            └── log_utils.py
```

**Rules**

- **One day = one folder** under `src/weekN/dayN/`.
- **On demand:** add `prompts/`, `data/`, `rag/`, `agents/`, `tools/` *inside* that day folder when the lesson requires it.
- **`src/setup/`** is the only shared area outside `weekN/dayN/`.
- **`.backup/`** holds frozen copies of older layouts (full `docs/weeks/`, extra notebooks, etc.).
