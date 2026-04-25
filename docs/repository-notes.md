# Repository Notes

## Cleanup Baseline

- Keep the MVP focused on discovery, risk review, and GDPR-style request generation.
- Keep secrets in local environment files only; commit examples, never real credentials.
- Keep email handling metadata-first: do not persist raw email bodies or attachments.
- Keep privacy and security documentation close to implementation decisions.
- Prefer small, reviewable backend changes with tests for security-sensitive behavior.

## Near-Term Maintenance

- Fill in the existing documentation placeholders before adding broad product surface area.
- Add test coverage around configuration loading, health checks, and future request workflows.
- Add explicit data retention rules before introducing persistent user data.
- Add structured logging that avoids personal data and secrets.
