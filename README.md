# CLINK — Smart Outpatient Triage and Scheduling

CLINK is a final-year project exploring how machine learning can support outpatient symptom triage and appointment scheduling. It provides patient, doctor, and administrator workflows. A Random Forest model classifies urgency and suggests a specialist based on submitted symptoms.

> **Research prototype:** CLINK is for academic demonstration only. It is not a medical device, does not provide a diagnosis, and must not be used for real clinical decisions or real patient data.

## Features

- Symptom submission and AI-assisted urgency classification
- Suggested specialist based on submitted symptoms
- Patient appointment booking and history
- Doctor case queue and appointment management
- Admin tools for user and schedule management
- Role-based access for patients, doctors, and administrators

## Technology

- Python 3.11+, Flask, SQLAlchemy, Flask-Login
- scikit-learn, NumPy, and pandas
- Jinja2, HTML, CSS, and JavaScript
- SQLite for local development; PostgreSQL/Supabase for deployment
- Vercel serverless entry point: api/index.py

## Run locally

### Requirements

- Python 3.11 or newer
- pip

### 1. Clone the repository and create a virtual environment

```bash
git clone https://github.com/Shams742/CLINK.git
cd CLINK
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
./.venv/Scripts/Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Configure environment variables

Copy the example file:

```powershell
Copy-Item code/.env.example code/.env
```

Or on macOS/Linux:

```bash
cp code/.env.example code/.env
```

Edit code/.env and set a unique SECRET_KEY. For local development, leave DATABASE_URL unset to use the local SQLite database. Never put production credentials in this file or commit code/.env.

### 3. Create a local database and optional sample data

```bash
cd code
python create_db.py
python seed_data.py
```

Only seed a disposable local database. Do not run the seed script against production or any database containing real patient information. Demo credentials are intentionally not listed here; see seed_data.py for local-only sample account details.

### 4. Start the app

From the code directory:

```bash
python run.py
```

Then open http://localhost:5000.

## Tests

From the code directory, run:

```bash
pytest tests/
```

## Deployment

The repository includes Vercel configuration. Set SECRET_KEY and DATABASE_URL in the hosting provider’s environment settings; never commit production values. Check the provider’s deployment settings before connecting or changing branches, since updates to the production branch may trigger a deployment.

## Dataset

The model uses the symptom/disease dataset at code/app/ai/data2/dataset.csv. The original source and license are not identified in the project documentation. Verify the dataset’s source and redistribution terms before reusing or redistributing it.

## License and project paper

No open-source license is specified. Contact the project author before reusing or redistributing the code or included materials. The project paper, CLINK_Short_Paper.docx, is also included in this repository; review it to ensure it contains no information you want kept private.
