from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.integration_log import create_integration_log, get_integrations_logs
from app.schemas.integration_log import IntegrationLogCreate, IntegrationOut
from typing import List

router = APIRouter()


@router.post("/", response_model=IntegrationOut)
def create_integration_endpoint(integration: IntegrationLogCreate, db: Session = Depends(get_db)):
    return create_integration_log(db, integration)



@router.get("/", response_model=List[IntegrationOut])
def list_integrations_endpoint(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return get_integrations_logs(db, skip=skip, limit=limit)
