from api.airline.airlines_router import router as airlines_router
from api.flight.flights_router import router as flights_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(
    airlines_router,
    prefix="/api"
)

api_router.include_router(
    flights_router,
    prefix="/api"
)
