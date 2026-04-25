# Security Policy

## Security Philosophy

Privacy Guardian is built as a privacy-first SaaS MVP. The project should minimise personal data, avoid unnecessary sensitive storage, and make security-relevant actions auditable.

## Current Security Scope

The current repository includes:

- FastAPI backend foundation.
- Environment-based configuration.
- SQLAlchemy models.
- Alembic migrations.
- Audit logging service.
- Demo-safe API endpoints.
- Static frontend dashboard.

The current repository does not include:

- Authentication.
- OAuth.
- External email API integrations.
- AI processing.
- Production deployment configuration.

## Sensitive Data Rules

Do not commit or store:

- `.env` files.
- Real credentials.
- Access tokens.
- Email bodies.
- Email attachments.
- Raw mailbox exports.
- Production database dumps.

Audit events must stay structured and must not contain raw sensitive content.

## Reporting Security Issues

For a real deployment, security reports should be sent through a private responsible disclosure channel. Until then, issues should be tracked privately and fixed before public release.

## Future Security Controls

Planned controls include:

- Authentication and user verification.
- Role and ownership checks.
- Rate limiting.
- Request template controls.
- Secret scanning in CI.
- Dependency scanning.
- Structured logging with redaction.
- Data retention and deletion enforcement.
- Production security headers and deployment hardening.
