# Privacy Guardian Interview Notes

## 1. 60-Second Project Pitch

Privacy Guardian is a security-first privacy SaaS MVP that helps individuals understand which organisations may hold their personal data, assess privacy risk, and prepare GDPR-style data rights requests.

The project is deliberately scoped as a narrow MVP. Instead of trying to automate every privacy task immediately, it starts with a secure backend foundation, clear documentation, privacy guardrails, and minimal data models. The main design principle is data minimisation: the system should not store email bodies, attachments, secrets, or unnecessary personal data.

For cybersecurity and GRC roles, this project demonstrates that I can think beyond code. I considered privacy-by-design, auditability, threat modelling, abuse cases, secure configuration, and future compliance evidence before expanding features.

## 2. Technical Architecture Explanation

The current architecture is an early FastAPI backend with a simple and maintainable structure:

- `backend/main.py` creates the FastAPI application.
- `app/api/health.py` exposes a basic `GET /health` endpoint.
- `app/core/config.py` handles environment-based configuration.
- `app/core/logging.py` provides a minimal logging setup.
- `app/db/base.py` defines the SQLAlchemy declarative base for future database migrations.
- `app/models/user.py` defines a minimal user model.
- `app/models/audit_event.py` defines structured audit events.
- `app/models/detected_company.py` and `app/models/privacy_request.py` define the first MVP workflow entities.
- `app/api/demo.py` exposes demo-safe workflow endpoints.

PostgreSQL support and Alembic migration scaffolding are present, but the app does not require a database for health checks or demo endpoint tests. That keeps local development simple while preserving a realistic path to production.

## 3. Security And Privacy-By-Design Explanation

The main security design choice is to minimise data collection and avoid sensitive storage by default.

Current privacy guardrails include:

- No raw email body storage.
- No attachment storage.
- No hardcoded secrets.
- No AI features yet.
- No external email API integrations yet.
- No authentication added before the data model and threat model are clearer.
- Audit events are structured and do not include raw free-text payloads.

This approach reduces the risk of accidental data exposure. It also makes the system easier to audit because sensitive workflows are not hidden inside broad, uncontrolled data fields.

## 4. GDPR And ISO Standards Alignment Explanation

The project is not claiming formal compliance yet, but it is designed with relevant principles in mind.

GDPR alignment:

- Data minimisation: only user email is planned at this stage.
- Purpose limitation: the MVP focuses on privacy discovery and rights-request workflows.
- Storage limitation: future work will define retention and deletion rules before storing more user data.
- Accountability: audit events are included early to support traceability.
- Data subject rights: the product concept supports GDPR-style access, deletion, and rectification request workflows.

ISO alignment:

- ISO/IEC 27001: the project reflects early security governance thinking through documentation, risk awareness, access-control planning, and secure configuration.
- ISO/IEC 27002: the design considers controls around logging, secure development, information classification, and protection of sensitive information.
- ISO/IEC 27701: the privacy-focused design maps naturally to privacy information management concepts such as minimisation, purpose limitation, and privacy control documentation.

In an interview, I would explain that this is not a certified system, but it shows I can apply compliance principles during design rather than treating them as an afterthought.

## 5. Threat Model Explanation

The main assets are:

- User email addresses.
- Audit records.
- Future generated data rights requests.
- Configuration and secrets.
- Future organisation and request metadata.

Important threat scenarios include:

- Accidental storage of raw email content or attachments.
- Secrets committed to GitHub.
- Excessive logging of personal data.
- Unauthorised access to user request history.
- Abuse of the service to send spam or harassing requests.
- Injection or tampering in future request templates.
- Over-broad database fields that become uncontrolled sensitive-data stores.

The current mitigation approach is to keep the data model narrow, avoid external integrations, ignore secret files, and document risky areas before implementing them.

## 6. Abuse-Case Explanation

Abuse cases are ways the system could be misused even if the normal user flow works.

Examples include:

- A user tries to use the platform to send abusive messages disguised as GDPR requests.
- A malicious user submits another person's email address.
- Someone tries to store secrets or sensitive text inside audit event fields.
- An attacker attempts to trigger excessive logging of personal data.
- A future integration accidentally imports full mailbox content instead of metadata.

The MVP reduces these risks by not connecting email APIs, not storing email bodies, not storing attachments, and keeping audit events structured. Future work should add validation, rate limiting, authentication, user verification, request-template controls, and abuse monitoring.

## 7. Why This Is A Real-World SaaS Idea

Privacy Guardian addresses a real user problem: people often do not know who holds their data or how to exercise their rights under privacy law.

It also reflects real organisational needs:

- Privacy rights are becoming more visible to consumers.
- Users want simpler ways to manage data rights requests.
- Companies need clearer and more standardised communication from data subjects.
- Security teams need systems that minimise collected personal data.
- GRC teams care about auditability, evidence, and documented controls.

The SaaS idea is realistic because it combines user value with compliance-aware workflows, but the MVP must stay narrow to avoid creating new privacy risks.

## 8. What Has Been Completed So Far

Completed work includes:

- Repository cleanup and safer `.gitignore` rules.
- Professional README with backend setup and privacy guardrails.
- `PROJECT_SUMMARY.md` for GitHub, CV, LinkedIn, and interview use.
- `docs/repository-notes.md` with project guardrails.
- FastAPI backend foundation.
- Working `GET /health` endpoint.
- Environment-based configuration without requiring PostgreSQL yet.
- Minimal logging setup.
- `.env.example` for safe local setup.
- SQLAlchemy declarative base.
- Minimal `User`, `AuditEvent`, `DetectedCompany`, and `PrivacyRequest` models.
- Alembic migration scaffold and first migration.
- Audit logging service foundation.
- Demo-safe backend workflow endpoints.
- Static frontend dashboard prototype.
- GitHub push to the main branch.

## 9. What I Would Build Next

The next steps should remain security-focused:

1. Complete `docs/data-handling-rules.md`.
2. Complete `docs/threat-model.md`.
3. Complete `docs/abuse-cases.md`.
4. Add automated tests for config and health endpoints.
5. Replace demo data with database-backed persistence.
6. Expand the audit event taxonomy and validation.
7. Add data retention and deletion rules.
8. Add authentication and user verification.
9. Build the first controlled production data rights request workflow.
10. Add CI checks for tests, dependency scanning, and secret scanning.

I would not add AI features, external mailbox integrations, or broad automation until the privacy model, retention policy, and abuse controls are stronger.

## 10. Possible Interview Questions And Strong Answers

### What is Privacy Guardian?

Privacy Guardian is a privacy-focused SaaS MVP that helps users understand which organisations may hold their data and prepare GDPR-style data rights requests. I built the early foundation around data minimisation, auditability, and secure backend design.

### Why did you choose FastAPI?

FastAPI is lightweight, modern, and suitable for building clear API boundaries quickly. It also works well with Pydantic and SQLAlchemy, which helps create maintainable backend code for an MVP.

### What makes this project security-first?

I defined security and privacy constraints before adding features. For example, the project avoids storing email bodies, attachments, secrets, and uncontrolled audit payloads. I also added documentation, safe environment handling, structured models, and auditability early.

### How does this project relate to GRC?

It connects technical implementation with governance concepts. The project considers GDPR principles, audit trails, documentation, risk scenarios, abuse cases, and future control evidence. It shows I can think about security as both an engineering and governance problem.

### Is the project GDPR compliant?

I would not claim full compliance at this stage. It is an MVP foundation designed with GDPR principles in mind, especially data minimisation, purpose limitation, storage limitation, accountability, and data subject rights.

### Why not add authentication immediately?

Authentication is important, but I wanted to define the data model, privacy boundaries, and threat assumptions first. Adding authentication too early can create a false sense of completeness if logging, retention, data minimisation, and audit design are not ready.

### Why did you avoid storing email bodies and attachments?

Email bodies and attachments can contain highly sensitive personal data, special category data, credentials, and third-party information. Avoiding storage reduces legal, security, and operational risk.

### What is the purpose of the AuditEvent model?

The `AuditEvent` model supports traceability. It records structured metadata about important actions without storing raw sensitive content. This supports accountability while respecting data minimisation.

### What are the biggest risks in this project?

The biggest risks are over-collection of personal data, accidental logging of sensitive information, abuse of request-generation features, weak authentication in future versions, and unclear retention policies. The current MVP intentionally avoids high-risk integrations until those risks are addressed.

### How would you improve the project next?

I would replace the demo endpoints with database-backed workflows, add authentication and user verification, enforce retention rules, and add CI security checks. After that, I would build one narrow production request-generation workflow using controlled templates.

### How would you explain this on your CV?

I would describe it as a security-first privacy SaaS MVP built with FastAPI and SQLAlchemy, designed around GDPR principles, data minimisation, auditability, and privacy-by-design. I would highlight the backend foundation, documentation, threat modelling, and GRC relevance.

### What did you learn from building it?

I learned that privacy engineering is not just about adding controls after development. It requires careful decisions about what not to collect, what not to store, and how to document risk before building features.
