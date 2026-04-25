# Privacy Guardian Project Summary

## Executive Summary

Privacy Guardian is a security-first B2C privacy SaaS MVP that helps individuals understand which organisations may hold their personal data, assess privacy risk, and prepare GDPR-style data rights requests.

The project is built around a simple idea: a privacy product should not create a new privacy problem. The MVP therefore focuses on data minimisation, auditability, controlled request workflows, and clear documentation before adding high-risk features such as mailbox integrations, AI, OAuth, or automated request sending.

This repository now demonstrates a professional early-stage SaaS foundation suitable for GitHub, CV use, LinkedIn discussion, and cybersecurity/GRC interviews.

## The Problem It Solves

Individuals often do not know:

- Which organisations hold their personal data.
- How risky or important those organisations may be.
- How to exercise GDPR-style data rights.
- How to keep track of requests they have made.
- How to avoid exposing even more sensitive data while trying to protect their privacy.

Privacy Guardian addresses this by proposing a guided workflow where a user can review detected or manually added companies, see privacy-risk indicators, create controlled data rights requests, and track status in an auditable way.

## Real-World Value

This is a realistic SaaS idea because privacy rights are legally meaningful but hard for ordinary users to exercise. Many people know they have GDPR rights, but they do not know how to identify relevant organisations, write appropriate requests, prioritise risk, or maintain records.

The project also reflects real security and GRC concerns:

- Data minimisation reduces breach impact.
- Structured audit events support accountability.
- Safe configuration reduces secret leakage risk.
- Clear documentation supports governance and review.
- Deferring risky integrations reduces early product risk.

## MVP Scope

The MVP is intentionally narrow. It is designed to prove the core workflow without over-collecting data.

Current MVP scope includes:

- FastAPI backend foundation.
- Health endpoint.
- Demo-safe company discovery endpoints.
- Demo-safe risk score endpoint.
- Demo-safe privacy request creation and status tracking.
- SQLAlchemy privacy-safe models.
- Alembic migration scaffold and first migration.
- Audit logging service foundation.
- Static frontend dashboard prototype.
- Professional project documentation.
- Pytest coverage for the health and demo endpoints.

Explicitly out of scope for now:

- Authentication and OAuth.
- Real external email API connections.
- AI-generated requests or advice.
- Automated request sending.
- Production PostgreSQL deployment.
- Storage of email bodies or attachments.
- Browser extensions or large integrations.

## Repository Structure

```text
backend/                  FastAPI backend, models, tests, Alembic setup
backend/app/api/          API routes including health and demo MVP endpoints
backend/app/core/         Configuration and logging
backend/app/db/           SQLAlchemy base and database session helper
backend/app/models/       Privacy-safe SQLAlchemy models
backend/app/services/     Audit logging service
backend/tests/            Backend pytest tests
docs/                     Product, architecture, threat, compliance, and data notes
frontend/                 Static MVP dashboard prototype
PROJECT_SUMMARY.md        Professional project overview
INTERVIEW_NOTES.md        Interview preparation notes
ROADMAP.md                Phased product and engineering roadmap
SECURITY.md               Security policy and future controls
PRIVACY_DESIGN.md         Privacy-by-design explanation
PRODUCT_STRATEGY_REVIEW.md Product strategy critique and 90-day roadmap
```

## Backend Foundation

The backend is built with FastAPI and keeps the structure deliberately simple:

- `backend/main.py` creates the FastAPI application.
- `app/api/health.py` exposes `GET /health`.
- `app/api/demo.py` exposes demo-safe MVP workflow endpoints.
- `app/core/config.py` loads environment-based settings.
- `app/core/logging.py` provides minimal logging setup.
- `app/db/base.py` defines SQLAlchemy metadata for migrations.
- `app/db/session.py` prepares database session handling without requiring PostgreSQL for health checks or tests.
- `app/models/` contains migration-ready SQLAlchemy models.
- `app/services/audit_logging.py` contains the first audit logging service.

The backend can run locally and return:

```json
{"status":"ok"}
```

## Demo-Safe API Workflow

The MVP demo API includes:

```text
GET  /health
GET  /api/v1/demo/companies
GET  /api/v1/demo/companies/{company_id}
GET  /api/v1/demo/companies/{company_id}/risk
POST /api/v1/demo/companies/{company_id}/privacy-requests
GET  /api/v1/demo/privacy-requests/{request_id}
```

These endpoints are intentionally demo-safe:

- They use placeholder data.
- They do not connect to real email accounts.
- They do not store raw email content.
- They do not store attachments.
- They do not send requests externally.
- They demonstrate production-friendly API shape without pretending production controls are complete.

## Data Models

The first SQLAlchemy models are privacy-safe and migration-ready.

### User

Stores only the minimum user identity needed at this stage:

- `id`
- `email`
- `created_at`
- `updated_at`

No passwords, tokens, profile details, or unnecessary personal data are included yet.

### AuditEvent

Supports security-relevant traceability without becoming a sensitive data dump.

Fields include:

- `id`
- `user_id`
- `event_type`
- `target_type`
- `target_id`
- `created_at`
- `updated_at`

It intentionally avoids raw email bodies, attachments, secrets, request content, and free-text sensitive payloads.

### DetectedCompany

Represents an organisation that may hold user data.

Fields include:

- `id`
- `user_id`
- `name`
- `domain`
- `risk_level`
- `risk_score`
- `source`
- `created_at`
- `updated_at`

### PrivacyRequest

Represents a controlled data rights request workflow.

Fields include:

- `id`
- `user_id`
- `company_id`
- `request_type`
- `status`
- `template_reference`
- `request_summary`
- `created_at`
- `updated_at`

The model stores request metadata and template references, not raw email bodies or attachments.

## Database And Migrations

The project includes PostgreSQL-ready database support without hardcoded credentials.

Implemented:

- `DATABASE_URL` loaded from environment variables.
- `.env.example` with placeholder local values only.
- SQLAlchemy declarative base.
- Alembic scaffold.
- First migration for:
  - `users`
  - `audit_events`
  - `detected_companies`
  - `privacy_requests`

The backend does not require PostgreSQL for local health checks or tests. This keeps development simple while preserving a realistic path to database-backed production workflows.

## Audit Logging Service

The audit logging service supports controlled security-relevant events, including:

- `user_created`
- `login_attempt`
- `email_connection_requested`
- `scan_started`
- `scan_completed`
- `privacy_request_created`
- `privacy_request_sent`

The implementation is intentionally structured. It records event type and target metadata, not sensitive raw content.

## Frontend Prototype

The `frontend/` folder contains a static dashboard prototype with:

- Landing section.
- Detected companies dashboard.
- Company detail section.
- Privacy request creation section.
- Request status section.
- Privacy-by-design messaging.

The design is calm and trust-focused rather than flashy. It is intended to show the user journey without adding frontend build complexity too early.

## Security-First Design Approach

Privacy Guardian is designed around the principle that privacy tooling should reduce risk, not concentrate it.

Current guardrails:

- Do not store raw email bodies.
- Do not store email attachments.
- Do not hardcode secrets.
- Do not add AI features yet.
- Do not connect external email APIs yet.
- Keep audit logs structured.
- Keep `.env` files ignored.
- Use `.env.example` only for safe placeholders.
- Keep the MVP narrow and reviewable.

Security reasoning:

- Avoiding email body and attachment storage reduces breach impact.
- Avoiding AI at this stage avoids unclear processing, hallucination, and data transfer risks.
- Avoiding external email APIs prevents over-collection from mailboxes.
- Structured audit events support traceability without sensitive payloads.
- Documentation creates an evidence base for future GRC review.

## GDPR And Privacy Alignment

The project is not claiming formal legal compliance. It is designed with GDPR principles in mind.

Relevant GDPR principles:

- Lawfulness, fairness, and transparency.
- Purpose limitation.
- Data minimisation.
- Accuracy.
- Storage limitation.
- Integrity and confidentiality.
- Accountability.

Relevant data subject rights:

- Right of access.
- Right to rectification.
- Right to erasure.
- Right to object.
- Right to restrict processing.

The product concept supports these rights by helping users create controlled, understandable requests.

## ISO And GRC Alignment

The project can be explained in relation to security and privacy governance standards.

ISO/IEC 27001:

- Security governance and risk-based thinking.
- Control planning before production deployment.
- Protection of information assets.
- Secure configuration and access-control planning.

ISO/IEC 27002:

- Secure development practices.
- Logging and monitoring considerations.
- Information classification.
- Protection from secret leakage.
- Supplier and integration risk awareness.

ISO/IEC 27701:

- Privacy information management.
- Data minimisation.
- Purpose limitation.
- Privacy control documentation.
- Accountability for personal data processing.

This is useful for GRC interviews because the project shows how technical design, documentation, and risk management connect.

## Documentation Completed

The repository now includes:

- `README.md`: setup, endpoints, tests, migrations, frontend, and guardrails.
- `PROJECT_SUMMARY.md`: full professional project overview.
- `INTERVIEW_NOTES.md`: cybersecurity/GRC interview preparation.
- `ROADMAP.md`: phased roadmap.
- `SECURITY.md`: security policy and future controls.
- `PRIVACY_DESIGN.md`: privacy-by-design explanation.
- `PRODUCT_STRATEGY_REVIEW.md`: product critique and 90-day roadmap.
- `docs/product-scope.md`
- `docs/data-handling-rules.md`
- `docs/threat-model.md`
- `docs/abuse-cases.md`
- `docs/architecture.md`
- `docs/core-user-flow.md`
- `docs/compliance-assumptions.md`
- `docs/tech-decisions.md`
- `docs/repository-notes.md`

## Testing Completed

Pytest coverage currently includes:

- Health endpoint test.
- Demo companies endpoint test.
- Demo risk score endpoint test.
- Demo privacy request creation and status tracking test.

Current test result:

```text
4 passed
```

## Current Project Status

Privacy Guardian is now a portfolio-ready MVP foundation.

Completed:

- Professional repository structure.
- GitHub-ready documentation.
- FastAPI backend foundation.
- Health endpoint.
- Demo-safe workflow endpoints.
- SQLAlchemy models.
- Alembic migration scaffold and initial migration.
- Audit logging service foundation.
- Pytest test coverage.
- Static frontend prototype.
- Security and privacy design documents.
- Product strategy review.
- Interview notes.

Not completed yet:

- Authentication.
- User verification.
- Production database deployment.
- Database-backed endpoint persistence.
- Data retention enforcement.
- Real request sending.
- External email integrations.
- CI security checks.
- Production deployment.
- Legal review.

## Next Technical Steps

Recommended next implementation steps:

1. Add CI for tests and secret scanning.
2. Replace demo in-memory endpoint data with database-backed workflows.
3. Add authentication and email verification.
4. Add ownership checks for all user data.
5. Define and enforce retention and deletion rules.
6. Expand audit event taxonomy and validation.
7. Add request template governance.
8. Add rate limiting and abuse monitoring.
9. Improve frontend integration with backend APIs.
10. Conduct a DPIA-style privacy review before external integrations.

## Next Product Steps

Recommended product steps:

1. Validate the user problem with potential users.
2. Define the first real workflow: manual company entry plus request template.
3. Define transparent risk scoring criteria.
4. Draft privacy notice language.
5. Create an acceptable-use policy.
6. Decide whether the first market is UK GDPR, EU GDPR, or both.
7. Avoid AI and mailbox integrations until trust controls are mature.

## Interview Positioning

This project is strongest when explained as a security and GRC-minded engineering project, not just a coding project.

Good interview framing:

> Privacy Guardian is a privacy-by-design SaaS MVP that helps users identify organisations that may hold their personal data and prepare GDPR-style data rights requests. I built the early foundation with FastAPI, SQLAlchemy, Alembic, pytest, and a static frontend prototype. The important part is that I designed the system around data minimisation and auditability from the start: no raw email bodies, no attachments, no hardcoded secrets, no AI, and no external mailbox integrations at this stage. It demonstrates backend engineering, secure design, privacy governance, threat modelling, and GRC thinking.

Key points to highlight:

- You deliberately limited scope to reduce risk.
- You built models and audit logging around structured metadata.
- You considered GDPR and ISO principles.
- You documented threats, abuse cases, and privacy design.
- You can explain what is complete and what must happen before production.

## CV-Friendly Description

Security-first privacy SaaS MVP built with FastAPI, SQLAlchemy, Alembic, pytest, and a static frontend prototype. Designed around GDPR principles, data minimisation, auditability, and privacy-by-design. Implemented health checks, demo-safe privacy workflow APIs, migration-ready data models, audit logging foundation, professional documentation, and cybersecurity/GRC interview materials.
