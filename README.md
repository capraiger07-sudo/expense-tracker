# Expense Tracker

A personal expense tracking app built with FastAPI, Streamlit and PostgreSQL.

## Tech Stack
- Backend: FastAPI
- Frontend: Streamlit
- Database: PostgreSQL

## Setup Instructions

1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate`
4. Install libraries: `pip install -r requirements.txt`
5. Create `.env` file from `.env.example`
6. Run backend: `uvicorn app.main:app --reload`
7. Run frontend: `streamlit run app.py`