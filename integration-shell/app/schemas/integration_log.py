from pydantic import BaseModel





class IntegrationBase(BaseModel):
    name: str
    description: str | None = None
    active: bool = True

class IntegrationLogCreate(IntegrationBase):
    pass

class IntegrationOut(IntegrationBase):
    id: int

    class Config:
        from_attributes = True
