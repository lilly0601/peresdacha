from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.airline.airlines_schemas import AirlineCreate, AirlineRead
from business_logic.airlines.airlines_service import AirlineService
from data_access.airlines.airlines_repository import AirlineRepository

from data_access.db.session import get_db

router = APIRouter()

def get_airlines_service(db: AsyncSession = Depends(get_db)) -> AirlineService:
    repo = AirlineRepository(db)
    return AirlineService(repo)

@router.get("/all", response_model=list[AirlineRead])
async def get_airlines(
    service: AirlineService = Depends(get_airlines_service),
):
    return await service.get_airlines()

@router.post("/create", response_model=AirlineRead)
async def create_airlines(
    airline: AirlineCreate,
    service: AirlineService = Depends(get_airlines_service),
):
    try:
        return await service.create(airline)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    