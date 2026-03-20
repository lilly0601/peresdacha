from fastapi import HTTPException
from data_access.airlines.airlines_repository import AirlineRepository
from data_access.db.models.airline import Airline
from api.airline.airlines_schemas import AirlineRead, AirlineCreate
from uuid import UUID

class AirlineService:
    def __init__(self, repo: AirlineRepository):
        self.repo = repo

    async def get_airlines(self):
        return await self.repo.get_all()
    
    async def get_by_id(self, airline_id: UUID):
        airline = await self.repo.get_by_id(airline_id)

        if not airline:
            raise HTTPException(status_code=404, detail="Airline not found")
        return airline
    
    async def create(self, data: AirlineCreate):
        airline = Airline(
            name=data.name,
            country=data.country,
            iata_code=data.iata_code
        )

        return await self.repo.create(airline)
