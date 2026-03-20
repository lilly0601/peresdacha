from sqlalchemy import (Column, String, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship

from data_access.db.base import Base

class Flight(Base):
    __tablename__ = "flights"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    flight_number = Column(String(50))
    destination = Column(String(255), nullable=False)

    airline_id = Column(UUID(as_uuid=True), ForeignKey("airlines.id"))
    airline = relationship("Airline", back_populates="flights")