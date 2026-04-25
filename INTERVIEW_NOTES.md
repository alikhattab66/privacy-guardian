# Privacy Guardian Interview Notes

These notes are designed to help explain Privacy Guardian confidently in cybersecurity, GRC, privacy, and security placement interviews. The tone should be professional and honest: this is a portfolio-ready MVP foundation, not a production-certified privacy platform.

## 1. 60-Second Project Pitch

Privacy Guardian is a security-first B2C privacy SaaS MVP that helps users understand which organisations may hold their personal data, assess privacy risk, and prepare GDPR-style data rights requests.

I built it as a privacy-by-design project rather than just a normal web app. The main idea is that a privacy tool should not create a new privacy risk. So the MVP deliberately avoids storing raw email bodies, attachments, secrets, or unnecessary personal data. It also avoids AI and external mailbox integrations at this stage.

Technically, the project uses FastAPI, SQLAlchemy, Alembic, pytest, and a static frontend prototype. It includes a health endpoint, demo-safe workflow endpoints, migration-ready models, an audit logging service foundation, and professional documentation covering security, privacy design, threat modelling, abuse cases, roadmap, and interview preparation.

For GRC and cybersecurity interviews, I would explain it as a project that shows secure engineering, privacy governance, risk awareness, documentation discipline, and product thinking.

## 2. Shorter Pitch For CV Or LinkedIn

Privacy Guardian is a privacy-by-design SaaS MVP built with FastAPI and SQLAlchemy to help users identify organisations holding their data and prepare GDPR-style rights requests. The project demonstrates secure backend foundations, data minimisation, auditability, Alembic migrations, pytest coverage, privacy-safe models, and GRC-focused documentation.

## 3. Technical Architecture Explanation

The architecture is intentionally simple and maintainable.

Backend:

- `backend/main.py` creates the FastAPI application.
- `app/api/health.py` provides `GET /health`.
- `app/api/demo.py` provides demo-safe MVP workflow endpoints.
- `app/core/config.py` handles environment-based settings.
- `app/core/logging.py` provides basic logging setup.
- `app/db/base.py` defines SQLAlchemy metadata.
- `app/db/session.py` prepares database session handling.
- `app/models/` contains migration-ready SQLAlchemy models.
- `app/services/audit_logging.py` contains the audit logging service foundation.
- `backend/alembic/` contains migration scaffolding and the first migration.
- `backend/tests/` contains pytest tests.

Frontend:

- `frontend/index.html` and `frontend/styles.css` provide a static dashboard prototype.
- The frontend shows the landing page, detected companies, company detail, privacy request creation, request status, and privacy-by-design messaging.

Important architectural decision:

The app does not require PostgreSQL for health checks or tests. `DATABASE_URL` is supported through environment variables for migrations and future database-backed workflows, but there are no hardcoded credentials.

## 4. Backend Endpoints To Explain

Current endpoints:

```text
GET  /health
GET  /api/v1/demo/companies
GET  /api/v1/demo/companies/{company_id}
GET  /api/v1/demo/companies/{company_id}/risk
POST /api/v1/demo/companies/{company_id}/privacy-requests
GET  /api/v1/demo/privacy-requests/{request_id}
```

How to explain them:

The endpoints are demo-safe. They show the intended API shape without connecting to real email accounts, sending real requests, or storing sensitive content. This makes the project realistic while keeping the MVP safe and reviewable.

## 5. Security And Privacy-By-Design Explanation

The core security decision is data minimisation.

The project avoids:

- Raw email body storage.
- Email attachment storage.
- Hardcoded secrets.
- AI features.
- External email APIs.
- Uncontrolled audit payloads.
- Real request sending before abuse controls exist.

The project includes:

- `.env.example` for safe local setup.
- Ignored real `.env` files.
- Structured audit events.
- Minimal models.
- Documentation for data handling, threats, abuse cases, privacy design, and security policy.
- Tests for the current API foundation.

How to explain this in an interview:

> I made security and privacy constraints part of the design from the beginning. Instead of building features first and trying to secure them later, I defined what the system must not collect or store. That reduced the risk of accidental sensitive data exposure and made the MVP easier to audit.

## 6. Data Minimisation Explanation

Data minimisation means collecting and storing only what is necessary for a defined purpose.

In Privacy Guardian:

- `User` stores only email and timestamps.
- `AuditEvent` stores event type and target metadata, not raw content.
- `DetectedCompany` stores company metadata and risk indicators.
- `PrivacyRequest` stores request type, status, and template reference, not full email bodies or attachments.

Strong answer:

> I designed the data model so that sensitive content does not have an easy place to land. For example, the audit event model does not include a generic JSON blob for arbitrary payloads. That is intentional because generic payloads often become accidental storage for secrets or personal data.

## 7. GDPR Alignment Explanation

I would not claim that the project is fully GDPR compliant. It is an MVP designed with GDPR principles in mind.

Relevant GDPR principles:

- Data minimisation: avoid unnecessary personal data.
- Purpose limitation: store data only for the privacy workflow.
- Storage limitation: future retention and deletion rules are planned.
- Integrity and confidentiality: avoid secrets and sensitive content in code or logs.
- Accountability: audit events support traceability.
- Transparency: documentation explains the system boundaries.

Relevant rights supported by the product idea:

- Right of access.
- Right to rectification.
- Right to erasure.
- Right to object.
- Right to restrict processing.

Strong answer:

> I would not say the project is legally compliant yet, because that would require formal review, privacy notices, retention rules, and production controls. What I can say is that the architecture is aligned with GDPR principles such as minimisation, purpose limitation, accountability, and data subject rights.

## 8. ISO And GRC Alignment Explanation

Privacy Guardian can be mapped to several security and privacy governance ideas.

ISO/IEC 27001:

- Risk-based security thinking.
- Protecting information assets.
- Secure configuration.
- Access-control planning.
- Governance documentation.

ISO/IEC 27002:

- Secure development.
- Logging and monitoring.
- Information classification.
- Secret management.
- Supplier and integration risk.

ISO/IEC 27701:

- Privacy information management.
- Data minimisation.
- Purpose limitation.
- Privacy controls and documentation.

Strong answer:

> The project helped me connect engineering decisions with GRC principles. For example, avoiding raw email storage is not just a coding decision; it is a risk control that supports minimisation, confidentiality, and accountability.

## 9. Threat Model Explanation

Important assets:

- User email addresses.
- Audit events.
- Company metadata.
- Privacy request metadata.
- Environment configuration.
- Future authentication state.
- Future request templates.

Important threats:

- Secrets committed to GitHub.
- Raw email content accidentally stored.
- Attachments imported by mistake.
- Sensitive data logged.
- Weak future authentication.
- User impersonation.
- Abuse of request workflows.
- Injection into request templates.
- Over-collection through future email integrations.

Current mitigations:

- `.env` ignored.
- `.env.example` uses placeholder values.
- No external email integration.
- No AI features.
- No raw body or attachment storage.
- Audit events are structured.
- Demo endpoints use placeholder data.
- Tests verify the basic API foundation.

Strong answer:

> The main threat I focused on was over-collection. In a privacy product, the biggest risk is that the tool becomes a central store of sensitive user data. So I designed the MVP to avoid raw email content, attachments, and broad payload fields.

## 10. Abuse-Case Explanation

Abuse cases are ways users or attackers could misuse the system.

Examples:

- A user tries to send abusive messages disguised as GDPR requests.
- A malicious person submits someone else's email address.
- Someone attempts to store secrets in metadata fields.
- A future mailbox integration imports full message bodies.
- A user creates high-volume requests against organisations.
- An attacker tries to infer user activity from request status.

Current controls:

- No real email sending.
- No external mailbox access.
- No attachment storage.
- No raw message storage.
- Demo-only endpoints.
- Structured audit events.

Future controls:

- Authentication.
- Email verification.
- Rate limiting.
- Abuse monitoring.
- Request template governance.
- User ownership checks.
- Retention and deletion enforcement.

Strong answer:

> I considered abuse cases early because a privacy rights tool could be misused to harass organisations or submit fraudulent requests. That is why automated sending, external email APIs, and open-ended messaging are deliberately deferred.

## 11. Why This Is A Real-World SaaS Idea

Privacy Guardian is realistic because privacy rights are useful but hard for everyday users to exercise.

Real-world reasons:

- People often do not know who holds their data.
- GDPR rights are powerful but procedural.
- Users need help prioritising which organisations matter.
- Standardised templates can reduce user confusion.
- Audit trails help users track actions.
- A trustworthy privacy posture is commercially important.

Commercial potential:

- Freemium consumer privacy dashboard.
- Paid request tracking.
- Premium privacy templates.
- Partnerships with consumer rights organisations.
- Privacy education and guided workflows.

But the product must earn trust. Trust would depend on minimisation, transparency, security controls, and not overpromising compliance.

## 12. What Has Been Completed So Far

Completed repository work:

- Professional README.
- Project summary.
- Interview notes.
- Roadmap.
- Security policy.
- Privacy design document.
- Product strategy review.
- Filled documentation in `docs/`.
- Safer `.gitignore`.
- `.env.example`.

Completed backend work:

- FastAPI app.
- Health endpoint.
- Demo-safe workflow endpoints.
- Environment-based config.
- Minimal logging.
- SQLAlchemy base.
- Database session helper.
- Alembic scaffold.
- Initial migration.
- Privacy-safe models.
- Audit logging service foundation.
- Pytest tests.

Completed frontend work:

- Static landing/dashboard prototype.
- Detected company cards.
- Company detail section.
- Privacy request creation section.
- Request status section.
- Privacy-by-design messaging.

Verification:

```text
4 backend tests passed
```

## 13. What I Would Build Next

Technical next steps:

1. Add CI for tests and secret scanning.
2. Replace demo data with database-backed endpoints.
3. Add authentication and email verification.
4. Add user ownership checks.
5. Add retention and deletion enforcement.
6. Expand audit event validation.
7. Add rate limiting.
8. Add controlled request templates.
9. Connect frontend to backend APIs.
10. Prepare production deployment hardening.

Product next steps:

1. Validate the problem with target users.
2. Define the first supported request types.
3. Create transparent risk scoring criteria.
4. Draft privacy notice and terms.
5. Decide initial jurisdiction focus: UK GDPR, EU GDPR, or both.

What I would delay:

- AI features.
- External mailbox scanning.
- Automated request sending.
- Browser extensions.
- Enterprise features.

## 14. Strong Interview Answers

### What is Privacy Guardian?

Privacy Guardian is a privacy-by-design SaaS MVP that helps users identify organisations that may hold their personal data and prepare GDPR-style rights requests. I built the foundation with FastAPI, SQLAlchemy, Alembic, pytest, and a static dashboard prototype, while prioritising data minimisation and auditability.

### Why is this relevant to cybersecurity or GRC?

It shows how security, privacy, compliance, and engineering connect. The project includes threat modelling, abuse-case thinking, audit logging, data handling rules, GDPR principles, ISO alignment, and secure configuration. It is not just a coding project; it is a governance-aware security project.

### What makes it security-first?

The project defines what must not be collected before adding features. It avoids raw email bodies, attachments, secrets, AI processing, and external email integrations. It also keeps audit events structured and uses environment-based configuration.

### Why did you not add authentication yet?

Authentication is essential, but I wanted to establish data boundaries, threat assumptions, audit design, and safe models first. Adding login too early can make a project look complete while privacy and retention risks remain unresolved.

### Why avoid AI features?

AI could be useful later, but it introduces risks around data sharing, hallucination, explainability, and user trust. For a privacy SaaS, AI should be delayed until the data governance model is strong.

### Why avoid storing email bodies and attachments?

Email bodies and attachments can contain highly sensitive personal data, credentials, financial data, health data, third-party data, and special category data. Not storing them greatly reduces breach impact and compliance risk.

### What is the purpose of AuditEvent?

`AuditEvent` supports accountability by recording structured security-relevant events such as user creation, login attempts, scan events, and privacy request actions. It intentionally avoids raw sensitive payloads.

### How would you make it production-ready?

I would add authentication, user verification, database-backed workflows, retention and deletion controls, CI security checks, rate limiting, abuse monitoring, production logging redaction, and a DPIA-style review before any external email integration.

### Is this GDPR compliant?

I would not claim full compliance yet. It is an MVP foundation designed around GDPR principles such as data minimisation, purpose limitation, accountability, and data subject rights. Formal compliance would require legal review, privacy notices, retention rules, user rights workflows, and production controls.

### What standards did you consider?

I considered GDPR principles, ISO/IEC 27001 for governance and risk management, ISO/IEC 27002 for security controls, and ISO/IEC 27701 for privacy information management.

### What was the most important design decision?

The most important decision was to keep the system metadata-first and avoid raw email content. That keeps the MVP useful while reducing the chance that the product becomes a high-risk personal data store.

### What are the biggest risks?

The biggest risks are over-collection, weak future authentication, unclear retention, abuse of request sending, inaccurate risk scoring, and loss of user trust.

### How would you explain the project in one sentence?

Privacy Guardian is a security-first privacy SaaS MVP that demonstrates how to build GDPR-style data rights workflows with data minimisation, auditability, and GRC-aware engineering from the start.

## 15. Interview Closing Statement

If asked what the project shows about me, I would say:

> This project shows that I can think like both an engineer and a security/GRC professional. I built a working technical foundation, but I also considered privacy principles, abuse cases, auditability, documentation, and what should be delayed until stronger controls exist. That is the kind of thinking I want to bring into a cybersecurity or GRC placement role.
