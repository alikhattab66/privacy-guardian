# Privacy Guardian

Privacy Guardian is a security-first B2C privacy SaaS for helping users discover organisations that may hold their personal data, assess privacy risk, and generate GDPR-style data rights requests.

The MVP should stay narrow: data discovery, risk review, request generation, and audit-friendly workflows. It should not store email bodies or attachments, hardcode secrets, or introduce AI features before the core privacy and security model is stable.

## Repository Structure

```text
backend/   FastAPI application, backend configuration, and backend tests
docs/      Product, architecture, threat model, and data-handling notes
frontend/  Placeholder for the user-facing application
infra/     Placeholder for deployment and infrastructure configuration
security/  Placeholder for security review artifacts and policies
tests/     Placeholder for cross-project tests
```

## Backend Setup

The backend currently exposes a minimal FastAPI app with a health endpoint. It does not connect to PostgreSQL yet and does not require authentication for local health checks.

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn main:app --reload
```

Keep local secrets in `backend/.env`. Do not commit real secrets or production credentials.

## Test The Health Endpoint

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

## Current Status

This repository is in early MVP setup. The backend skeleton exists, documentation placeholders are present, and the next implementation work should focus on a minimal, auditable privacy workflow before adding broader product features.
