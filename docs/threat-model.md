# Threat Model

## Assets

- User email addresses.
- Audit event records.
- Detected company metadata.
- Privacy request metadata.
- Environment configuration.
- Future authentication state.

## Threats

- Secrets committed to source control.
- Raw email content accidentally stored in logs or database fields.
- Unauthorised access to user privacy request history.
- Abuse of request workflows for harassment or spam.
- Injection into future request templates.
- Overbroad audit logging that captures sensitive content.
- External email API integrations importing too much data.

## Current Mitigations

- `.env` and virtual environments are ignored.
- `.env.example` contains placeholders only.
- No external email API integration exists.
- Demo endpoints use placeholder data.
- Audit events are structured and do not include raw payloads.
- Models are intentionally minimal.

## Future Mitigations

- Authentication and user ownership checks.
- Rate limiting.
- Request template validation.
- Data retention and deletion workflows.
- CI secret scanning.
- Dependency scanning.
- Production logging redaction.
