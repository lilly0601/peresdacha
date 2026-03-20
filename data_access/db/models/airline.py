from sqlalchemy import (Column, String, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship

from data_access.db.base import Base

class Airline(Base):
    __tablename__ = "airlines"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False, unique=True)
    country = Column(String(100))
    iata_code = Column(String(10))

    flights = relationship("Flight", back_populates="airline")

    # fff