# Privacy Guardian Project Summary

## What Privacy Guardian Is

Privacy Guardian is a security-first B2C privacy SaaS concept that helps individuals understand which organisations may hold their personal data, assess privacy risk, and prepare GDPR-style data rights requests.

The project is designed as a narrow, maintainable MVP rather than a broad privacy automation platform. Its early foundation prioritises data minimisation, auditability, and clear boundaries around what the system must not store.

## The Problem It Solves

Consumers often do not know which companies hold their personal data, what risks are associated with that data, or how to exercise their privacy rights in a structured way.

Privacy Guardian addresses this by giving users a guided workflow to:

- Identify organisations that may hold their personal information.
- Track privacy-related actions in an auditable way.
- Generate controlled GDPR-style data rights request content.
- Avoid unnecessary storage of sensitive material such as email bodies and attachments.

## MVP Scope

The MVP is intentionally focused on a small set of core workflows:

- Basic backend service health checks.
- Privacy-safe project and backend foundation.
- Minimal SQLAlchemy model layer for users and audit events.
- Documentation scaffolding for architecture, threat modelling, abuse cases, data handling, compliance assumptions, and product scope.
- Guardrails that prevent the project from drifting into risky areas too early.

The MVP explicitly does not include:

- Authentication or account security flows yet.
- PostgreSQL runtime connection or database migrations yet.
- External email API integrations.
- AI features.
- Storage of raw email bodies or attachments.

## Security-First Design Approach

Privacy Guardian is being built around privacy-by-design principles from the start:

- Collect only the data needed for the current workflow.
- Store no sensitive personal data beyond user email at this stage.
- Avoid raw message bodies, attachments, secrets, and open-ended audit payloads.
- Keep audit events structured and narrow.
- Keep environment-specific configuration outside source control.
- Use `.env.example` for safe local setup documentation.
- Keep real `.env` files, virtual environments, caches, and compiled Python files ignored.
- Preserve documentation as part of the security and product design process.

## Documentation Completed

The repository now includes a professional README and repository notes covering:

- Project purpose and positioning.
- MVP constraints.
- Backend setup instructions.
- Health endpoint testing instructions.
- Privacy and security guardrails.
- Repository structure.
- Near-term maintenance notes.

The docs folder also includes placeholders for important future security and product documentation:

- `docs/product-scope.md`
- `docs/data-handling-rules.md`
- `docs/threat-model.md`
- `docs/architecture.md`
- `docs/tech-decisions.md`
- `docs/abuse-cases.md`
- `docs/compliance-assumptions.md`
- `docs/core-user-flow.md`
- `docs/repository-notes.md`

## Backend Foundation Completed

The backend foundation is a simple FastAPI application with:

- A working `GET /health` endpoint returning `{"status": "ok"}`.
- Configuration handled through `app/core/config.py`.
- Minimal logging setup in `app/core/logging.py`.
- No dependency on PostgreSQL at application import time.
- No authentication added yet.
- No external email API integration.
- A SQLAlchemy declarative base for future Alembic migrations.
- Minimal `User` and `AuditEvent` models.

The first models are intentionally small:

- `User`: stores only `id`, `email`, and `created_at`.
- `AuditEvent`: stores structured event metadata only, with no raw email content, attachments, secrets, or free-text payloads.

## Standards And Regulations Considered

The project is designed with awareness of:

- UK GDPR and EU GDPR data subject rights.
- Data minimisation principles.
- Purpose limitation.
- Storage limitation.
- Accountability and auditability.
- Security-by-design and privacy-by-design expectations.

At this stage, the project is not presented as a compliance-certified product. The documentation and architecture are being prepared so future implementation can be reviewed against regulatory expectations before handling sensitive workflows.

## Current Project Status

Privacy Guardian is in early MVP foundation stage.

Completed so far:

- Repository cleanup and safer ignore rules.
- README improvements.
- Local environment example file.
- Backend health endpoint foundation.
- Minimal backend configuration and logging.
- SQLAlchemy base and first privacy-safe models.
- Basic repository notes and project summary.

Not completed yet:

- Authentication and account lifecycle.
- Database connection management.
- Alembic migrations.
- Full test suite.
- Data retention enforcement.
- Request generation workflow.
- Frontend implementation.
- Production deployment configuration.

## Next Technical Steps

Recommended next steps:

1. Fill in `docs/data-handling-rules.md` with explicit allowed, forbidden, retained, and deleted data categories.
2. Complete `docs/threat-model.md` and `docs/abuse-cases.md` before adding user-facing workflows.
3. Add tests for configuration loading and the health endpoint.
4. Introduce database session management without connecting to production services.
5. Add Alembic migrations for the existing models.
6. Define a strict audit event taxonomy.
7. Add data retention and deletion rules before storing user workflow data.
8. Design a narrow request-generation workflow using controlled templates.
9. Add authentication only after the data model and security assumptions are documented.
10. Add CI checks for tests, formatting, and secret safety.

## How To Explain This Project In Interviews

Privacy Guardian is a security-first privacy SaaS MVP focused on helping users understand and exercise their data rights. The project is intentionally scoped to avoid over-collecting sensitive information while building a maintainable backend foundation.

A concise interview explanation:

> Privacy Guardian is a privacy-by-design SaaS project that helps users identify organisations that may hold their personal data and prepare GDPR-style rights requests. I focused the early architecture on data minimisation, auditability, and secure backend foundations. The initial FastAPI backend includes configuration, logging, a health endpoint, and privacy-safe SQLAlchemy models for users and audit events. I deliberately avoided storing email bodies, attachments, secrets, or AI-generated content at this stage so the MVP remains narrow and reviewable.

Key points to highlight:

- Security and privacy constraints were defined before feature expansion.
- The backend avoids database and authentication complexity until the foundations are ready.
- Audit events are structured to prevent accidental storage of sensitive content.
- Documentation is treated as part of the engineering system, not an afterthought.
- The project demonstrates product thinking, backend architecture, and privacy-aware engineering discipline.
