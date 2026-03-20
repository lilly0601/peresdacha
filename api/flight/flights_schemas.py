from pydantic import BaseModel
from uuid import UUID

class FlightRead(BaseModel):
    id: UUID
    flight_number: str
    destination: str
    airline_id: UUID


class FlightCreate(BaseModel):
    flight_number: str
    destination: str
    airline_id: UUID

    class Config:
        from_attributes = True