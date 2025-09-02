# Python by Example — Python (Flask) Edition

This repository now contains two projects:

- `legacy_nextjs/` — the original Next.js TypeScript app (archived here)
- `python_app/` — a new Flask-based Python app providing the same core functionality: browse Python examples, view code with highlighting, explanation, and output

## Quick Start (Python app)

```bash
cd python_app
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py  # http://localhost:8000
```

## Run the Python app

Prerequisites: Python 3.10+

### Option A) Standard venv (recommended)

```bash
cd python_app
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py  # http://localhost:8000
```

### Option B) Using uv

```bash
# Clean up any previous venv
rm -rf python_app/.venv

# Optionally install/select a Python runtime managed by uv
uv python install 3.12

cd python_app
uv venv --python 3.12   # or simply: uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python app.py  # http://localhost:8000
```

### Option C) Using pyenv

```bash
# Ensure Python is built with ensurepip
PYTHON_CONFIGURE_OPTS="--with-ensurepip=install" pyenv install 3.12.5

cd python_app
pyenv local 3.12.5
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Flask CLI (optional)

```bash
export FLASK_APP=app.py FLASK_RUN_PORT=8000 FLASK_DEBUG=1
flask run
# Windows PowerShell
# $env:FLASK_APP='app.py'; $env:FLASK_RUN_PORT='8000'; $env:FLASK_DEBUG='1'; flask run
```

### Virtual environment quick reference

- Create/activate (macOS/Linux): `python -m venv .venv && source .venv/bin/activate`
- Create/activate (Windows PowerShell): `python -m venv .venv; .venv\Scripts\Activate.ps1`
- Deactivate: `deactivate`
- Upgrade pip (optional): `python -m pip install --upgrade pip`

### Troubleshooting: venv/ensurepip error

If you see an error like:

```
Error: Command '[...]/.venv/bin/python', '-m', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.
```

Root causes and fixes:

1) Mixed managers (uv + pyenv) or stale venv
- Fix: `rm -rf python_app/.venv` then use a single manager (either uv or pyenv) and recreate the venv.

2) Python built without ensurepip
- pyenv reinstall with ensurepip:
  `PYTHON_CONFIGURE_OPTS="--with-ensurepip=install" pyenv install 3.12.5 && pyenv local 3.12.5`

3) Environment variables interfering
- Unset: `unset PYTHONHOME PYTHONPATH`

4) Prefer uv for simplicity
- `uv python install 3.12 && (cd python_app && uv venv --python 3.12 && source .venv/bin/activate && uv pip install -r requirements.txt)`

Checks to verify the active interpreter:

```bash
which -a python
python -V
python -c "import sys; print(sys.executable)"
env | grep -E '^PYTHON(HOME|PATH)='
```

Tip: If pyenv is interfering in this repo, you can disable it locally:

```bash
cd python_app
pyenv local system  # use system Python in this folder
```

## Project Structure

```
legacy_nextjs/   # Archived Next.js (TypeScript) app
python_app/      # New Flask app
  ├── app.py
  ├── data/
  │   └── examples.json
  ├── static/
  │   └── styles.css
  └── templates/
      ├── base.html
      ├── index.html
      ├── example.html
      └── 404.html
```

## What’s included

- Uses the same `examples.json` data structure
- Index page lists examples sorted by `order`
- Detail pages show code (Prism.js highlighting), explanation, and output
- Copy-to-clipboard for code blocks

## Legacy Next.js app

To run the archived app:

```bash
cd legacy_nextjs
npm install
npm run dev
```

## License

MIT
