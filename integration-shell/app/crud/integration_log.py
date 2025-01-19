from sqlalchemy.orm import Session

from app.models.integration_log import IntegrationLog
from app.schemas.integration_log import LogIntegrationCreate



def create_integration_log(db: Session, integration: LogIntegrationCreate):
    db_integration = IntegrationLog(**integration.dict())
    db.add(db_integration)
    db.commit()
    db.refresh(db_integration)
    return db_integration


def get_integrations_logs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(IntegrationLog).offset(skip).limit(limit).all()
