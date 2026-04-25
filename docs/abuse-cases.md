# Abuse Cases

## Potential Abuse Scenarios

- A user tries to send abusive content disguised as a GDPR request.
- A user submits another person's email address.
- A malicious actor attempts to store secrets in metadata fields.
- A future mailbox integration imports full email bodies instead of metadata.
- An attacker probes demo endpoints for unexpected data exposure.
- A user creates excessive request volume against a company.

## Current Controls

- No real email sending.
- No external mailbox connection.
- No raw email body or attachment storage.
- Demo-only endpoint data.
- Structured audit events.

## Future Controls

- Authentication and email verification.
- Rate limiting.
- Request template governance.
- Abuse monitoring.
- User ownership checks.
- Clear acceptable-use policy.
