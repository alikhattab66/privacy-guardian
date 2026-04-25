# Architecture

## Current Components

- FastAPI backend in `backend/`.
- Static frontend prototype in `frontend/`.
- SQLAlchemy model layer.
- Alembic migration scaffold.
- Pytest test suite.
- Documentation for privacy, security, and roadmap decisions.

## Backend Structure

- `backend/main.py`: FastAPI app entry point.
- `app/api/health.py`: health endpoint.
- `app/api/demo.py`: demo-safe MVP endpoints.
- `app/core/config.py`: environment-based settings.
- `app/core/logging.py`: basic logging setup.
- `app/db/base.py`: SQLAlchemy declarative base.
- `app/db/session.py`: database session helper.
- `app/models/`: privacy-safe models.
- `app/services/audit_logging.py`: structured audit event service.

## Architecture Direction

The next major architecture step is to replace demo data with authenticated, database-backed workflows while preserving strict data minimisation and auditability.
