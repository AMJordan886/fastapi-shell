from fastapi import APIRouter
from app.api.v1.endpoints import items, integrations

router = APIRouter()

router.include_router(items.router, prefix="/items", tags=["Items"])
router.include_router(integrations.router, prefix="/integrations", tags=["Integrations"])
