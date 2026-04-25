# Privacy Guardian

Privacy Guardian is a security-first B2C privacy SaaS for helping users discover organisations that may hold their personal data, assess privacy risk, and generate GDPR-style data rights requests.

The MVP should stay narrow: data discovery, risk review, request generation, and audit-friendly workflows. It should not store email bodies or attachments, hardcode secrets, or introduce AI features before the core privacy and security model is stable.

## Repository Structure

```text
backend/   FastAPI application, backend configuration, and backend tests
docs/      Product, architecture, threat model, and data-handling notes
frontend/  Static MVP dashboard prototype
infra/     Placeholder for deployment and infrastructure configuration
security/  Placeholder for security review artifacts and policies
tests/     Placeholder for cross-project tests
```

## Backend Setup

The backend exposes a FastAPI app with a health endpoint and demo-safe MVP endpoints. It does not require PostgreSQL for local health checks or tests, and it does not include authentication yet.

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn main:app --reload
```

Keep local secrets in `backend/.env`. Do not commit real secrets or production credentials.

## Backend Endpoints

With the backend running locally:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

Demo-safe MVP endpoints:

```text
GET  /api/v1/demo/companies
GET  /api/v1/demo/companies/{company_id}
GET  /api/v1/demo/companies/{company_id}/risk
POST /api/v1/demo/companies/{company_id}/privacy-requests
GET  /api/v1/demo/privacy-requests/{request_id}
```

These endpoints use placeholder data only. They do not connect to external email APIs and do not store raw email content, attachments, or secrets.

## Run Tests

From the `backend` directory with the virtual environment activated:

```powershell
pytest
```

The test suite covers the health endpoint and demo-safe MVP endpoints without requiring PostgreSQL.

## Database And Migrations

PostgreSQL support is configured through `DATABASE_URL` in the environment. Use `backend/.env.example` as a template and keep real credentials in `backend/.env`.

To apply migrations after configuring a local PostgreSQL database:

```powershell
cd backend
alembic upgrade head
```

The first migration creates the privacy-safe foundation models:

- `users`
- `audit_events`
- `detected_companies`
- `privacy_requests`

## Frontend Prototype

Open `frontend/index.html` in a browser to view the static MVP dashboard prototype.

## Privacy And Security Guardrails

- Do not store raw email bodies.
- Do not store email attachments.
- Do not hardcode secrets or credentials.
- Do not add AI features until the MVP privacy model is reviewed.
- Minimise stored personal data and prefer derived metadata where possible.
- Keep audit trails for user-visible actions and outbound data-rights requests.
- Treat GDPR-style request generation as a controlled workflow, not an open-ended messaging system.

## Documentation

Start with these documents before expanding implementation:

- `docs/product-scope.md`
- `docs/data-handling-rules.md`
- `docs/threat-model.md`
- `docs/architecture.md`
- `docs/tech-decisions.md`
- `docs/abuse-cases.md`
- `docs/compliance-assumptions.md`
- `docs/core-user-flow.md`
- `PROJECT_SUMMARY.md`
- `INTERVIEW_NOTES.md`
- `ROADMAP.md`
- `SECURITY.md`
- `PRIVACY_DESIGN.md`
- `PRODUCT_STRATEGY_REVIEW.md`

## Current Status

This repository is in MVP foundation stage. It includes a FastAPI backend, tests, privacy-safe models, Alembic migration scaffolding, demo-safe endpoints, a static dashboard prototype, and portfolio-ready documentation. The next implementation work should replace demo data with authenticated, database-backed workflows while preserving data minimisation and auditability.
