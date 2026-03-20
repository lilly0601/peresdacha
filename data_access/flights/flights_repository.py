from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from data_access.db.models.flight import Flight

class FlightRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Flight]:
        result = await self.db.execute(select(Flight))
        return result.scalars().all()
    
    async def get_by_id(self, flight_id: UUID) -> Flight | None:
        result = await self.db.execute(select(Flight).where(Flight.id == flight_id))
        return result.scalar_one_or_none()
    
    async def create(self, flight: Flight) -> Flight:
        self.db.add(flight)
        await self.db.commit()
        await self.db.refresh(flight)

        return flight