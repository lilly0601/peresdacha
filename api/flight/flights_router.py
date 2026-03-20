from fastapi import APIRouter
from . import flights_api


router = APIRouter(
    prefix="/flights",
)

router.include_router(
    flights_api.router,
    tags=["flights"]
)