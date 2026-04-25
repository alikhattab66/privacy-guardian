# Data Handling Rules

## Allowed At Current Stage

- User email address.
- Structured audit metadata.
- Company name and domain.
- Risk level and risk score.
- Privacy request type, status, and template reference.

## Forbidden

- Raw email bodies.
- Email attachments.
- Mailbox exports.
- Secrets or access tokens.
- Production credentials.
- Free-text audit payloads containing sensitive personal data.

## Retention Direction

Retention rules are not implemented yet. Before production use, each data type must have a retention period, deletion path, and user-facing explanation.

## Logging Rule

Logs must not include raw personal data, email bodies, attachments, credentials, tokens, or generated request content.
