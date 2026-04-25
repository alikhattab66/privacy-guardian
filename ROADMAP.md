# Privacy Guardian Roadmap

## Product Principle

Privacy Guardian should remain narrow, auditable, and privacy-preserving. Features should be added only when they support the core workflow: helping a user identify organisations that may hold their data, understand privacy risk, and create controlled GDPR-style rights requests.

## Phase 1: Professional Repository Foundation

Status: Complete

- Professional README.
- Safer `.gitignore`.
- `.env.example` for local setup.
- Project summary.
- Interview notes.
- Repository notes.
- Clear privacy and security guardrails.

## Phase 2: Backend Foundation

Status: Complete

- FastAPI application.
- `GET /health` endpoint.
- Environment-based configuration.
- Minimal logging setup.
- No PostgreSQL dependency at import time.
- No authentication yet.

## Phase 3: Backend Tests

Status: Complete

- Pytest setup through backend requirements.
- Health endpoint test.
- Demo endpoint tests.
- No PostgreSQL required for tests.

## Phase 4: Privacy-Safe Models

Status: Complete

- `User`
- `AuditEvent`
- `DetectedCompany`
- `PrivacyRequest`

The models avoid raw email content, attachments, secrets, and uncontrolled sensitive payloads.

## Phase 5: Database And Migrations

Status: Complete for foundation

- SQLAlchemy database session module.
- Alembic scaffold.
- First migration for existing models.
- `DATABASE_URL` loaded from environment variables.
- No hardcoded credentials.

## Phase 6: Audit Logging

Status: Complete for foundation

- Audit logging service.
- Controlled security event types.
- Structured event metadata only.
- No sensitive payload logging.

## Phase 7: MVP Demo Workflow

Status: Complete for demo-safe API

- Demo detected companies endpoint.
- Demo risk score endpoint.
- Demo privacy request creation endpoint.
- Demo request status endpoint.
- No external email API connection.
- No sensitive data storage.

## Phase 8: Frontend Dashboard

Status: Complete for static MVP

- Landing view.
- Dashboard view.
- Company detail view.
- Privacy request creation view.
- Request status view.

## Phase 9: Portfolio Readiness

Status: Complete for current stage

- GitHub-ready documentation.
- CV and interview notes.
- Security and privacy design documents.
- Professional roadmap.

## Phase 10: Next 90 Days

1. Replace demo data with database-backed workflows.
2. Add authentication and verified user ownership.
3. Add retention and deletion enforcement.
4. Complete threat model and abuse-case documentation in more detail.
5. Add CI for tests and secret scanning.
6. Add request template governance.
7. Add rate limiting and abuse monitoring.
8. Add production deployment hardening.
9. Conduct a privacy impact assessment.
10. Defer AI and mailbox integrations until trust controls are mature.
