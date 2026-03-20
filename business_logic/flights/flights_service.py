from fastapi import HTTPException
from data_access.flights.flights_repository import FlightRepository
from data_access.db.models.flight import Flight
from api.flight.flights_schemas import FlightRead, FlightCreate
from uuid import UUID


class FlightService:
    def __init__(self, repo: FlightRepository):
        self.repo = repo


    async def get_flights(self):
        return await self.repo.get_all()
    
    async def get_by_id(self, flight_id: UUID):
        flight = await self.repo.get_by_id(flight_id)

        if not flight:
            raise HTTPException(status_code=404, detail="Flights not found")
        return flight
    
    async def create(self, data: FlightCreate):
        flight = Flight(
            flight_number=data.flight_number,
            destination=data.destination,
            airline_id = data.airline_id

        )

        return await self.repo.create(flight)
