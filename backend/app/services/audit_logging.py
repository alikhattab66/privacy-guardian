from sqlalchemy.orm import Session

from app.models.audit_event import AuditEvent


SECURITY_EVENT_TYPES = {
    "user_created",
    "login_attempt",
    "email_connection_requested",
    "scan_started",
    "scan_completed",
    "privacy_request_created",
    "privacy_request_sent",
}


class AuditLoggingService:
    def create_event(
        self,
        db: Session,
        *,
        user_id: int,
        event_type: str,
        target_type: str | None = None,
        target_id: str | None = None,
    ) -> AuditEvent:
        if event_type not in SECURITY_EVENT_TYPES:
            raise ValueError(f"Unsupported audit event type: {event_type}")

        event = AuditEvent(
            user_id=user_id,
            event_type=event_type,
            target_type=target_type,
            target_id=target_id,
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
