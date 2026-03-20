from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.flight.flights_schemas import FlightCreate, FlightRead
from business_logic.flights.flights_service import FlightService
from data_access.flights.flights_repository import FlightRepository

from data_access.db.session import get_db

router = APIRouter()

def get_flights_service(db: AsyncSession = Depends(get_db)) -> FlightService:
    repo = FlightRepository(db)
    return FlightService(repo)

@router.get("/", response_model=list[FlightRead])
async def get_flights(
    service: FlightService = Depends(get_flights_service),
):
    return await service.get_flights()

@router.post("/", response_model=FlightRead)
async def create_flights(
    flight: FlightCreate,
    service: FlightService = Depends(get_flights_service),
):
    try:
        return await service.create(flight)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    