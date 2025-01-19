from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base



class IntegrationLog(Base):
    __tablename__ = "integrations logs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    active = Column(Boolean, default=True)
