from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from data_access.db.models.airline import Airline

class AirlineRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Airline]:
        result = await self.db.execute(select(Airline))
        return result.scalars().all()
    
    async def get_by_id(self, airline_id: UUID) -> Airline | None:
        result = await self.db.execute(select(Airline).where(Airline.id == airline_id))
        return result.scalar_one_or_none()
    
    async def create(self, airline: Airline) -> Airline:
        self.db.add(airline)
        await self.db.commit()
        await self.db.refresh(airline)  

        return airline