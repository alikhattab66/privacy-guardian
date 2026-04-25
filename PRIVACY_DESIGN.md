# Privacy Design

## Privacy-By-Design Goals

Privacy Guardian is designed to help users exercise privacy rights without creating unnecessary new privacy risk.

The core privacy goals are:

- Collect the minimum data needed.
- Avoid storing high-risk content.
- Keep audit logs structured.
- Make retention and deletion explicit.
- Delay risky integrations until controls are mature.

## Data Minimisation

At the current stage, the backend models only require:

- User email.
- Structured audit metadata.
- Company metadata.
- Privacy request status and template references.

The system must not store:

- Raw email bodies.
- Email attachments.
- Secrets.
- Full mailbox exports.
- Uncontrolled free-text audit payloads.

## Purpose Limitation

Stored data should support only the MVP privacy workflow:

- Identifying organisations.
- Assessing privacy risk.
- Creating controlled rights requests.
- Tracking request status.
- Auditing security-relevant actions.

## Auditability

Audit events should record who performed an action, what type of action occurred, and which non-sensitive target was involved. They should not record raw request bodies or sensitive user content.

## GDPR Principles Considered

- Lawfulness, fairness, and transparency.
- Purpose limitation.
- Data minimisation.
- Accuracy.
- Storage limitation.
- Integrity and confidentiality.
- Accountability.

## Deferred Privacy Decisions

Before production use, the project needs:

- A retention schedule.
- User deletion workflows.
- Export workflows.
- Authentication and identity verification.
- Privacy notice wording.
- Data processing records.
- DPIA-style risk review.
