from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/status")
def get_status():
    return {"status": "running"}
