# FarmEasy — Run instructions

Quick steps to run this Django project locally (PowerShell on Windows):

1) Create / activate virtual environment (recommended)

```powershell
# from repo root (salman project)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies

```powershell
pip install -r requirements.txt
```

3) Apply migrations and create a superuser

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4) Run the development server

```powershell
python manage.py runserver 8000
```

Open http://127.0.0.1:8000/ in your browser.

Notes and troubleshooting
- The project ships pre-trained sklearn models saved with scikit-learn 1.5.0. To avoid unpickling warnings/errors, `requirements.txt` pins `scikit-learn==1.5.0`.
- If you see ImportError for a package, activate the venv and `pip install <package>`.
- To reproduce the exact environment for others, generate a `requirements.txt` with `pip freeze > requirements.txt` after installing packages.

Files added to help run locally:
- `requirements.txt` — pinned packages
- `scripts/run_dev.ps1` — helper PowerShell script to create venv, install deps, migrate and run server
- `check_env.py` — quick script to verify installed package versions (run with the venv active)