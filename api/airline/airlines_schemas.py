from pydantic import BaseModel
from uuid import UUID

class AirlineRead(BaseModel):
    id: UUID
    name: str
    country: str
    iata_code: str


class AirlineCreate(BaseModel):
    name: str
    country: str
    iata_code: str

    class Config:
        from_attributes = True