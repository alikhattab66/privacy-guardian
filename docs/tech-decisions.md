# Technical Decisions

## FastAPI

FastAPI is used for a clear, maintainable API foundation with strong typing and straightforward testing.

## SQLAlchemy

SQLAlchemy is used for migration-ready relational models. The initial models are intentionally minimal and privacy-safe.

## Alembic

Alembic is used for database migrations. `DATABASE_URL` is read from environment variables and no credentials are hardcoded.

## Static Frontend

The first frontend is static to demonstrate the product workflow without introducing frontend build complexity too early.

## Deferred Decisions

- Authentication provider.
- Production hosting.
- Email provider.
- AI usage.
- Request delivery workflow.
