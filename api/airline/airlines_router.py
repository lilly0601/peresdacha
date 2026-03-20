from fastapi import APIRouter
from . import airlines_api


router = APIRouter(
    prefix="/airlines",
)

router.include_router(
    airlines_api.router,
    tags=["airlines"]   

)