import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from data_access.db.models.airline import Airline
from data_access.db.models.flight import Flight
from data_access.db.session import AsyncSessionLocal

async def seed_airlines(db: AsyncSession):
    """Airline кестесін толтыру (егер жоқ болса)"""
    airlines_data = [
        {"name": "Fly Arystan", "country": "Kazakhstan"},
        {"name": "Air Astana", "country": "Kazakhstan"}
    ]

    for a in airlines_data:
        result = await db.execute(select(Airline).where(Airline.name == a["name"]))
        exists = result.scalar_one_or_none()
        if not exists:
            airline = Airline(name=a["name"], country=a["country"])
            db.add(airline)

    await db.commit()

async def seed_flights(db: AsyncSession):
    """Flight кестесін толтыру, Airline Foreign Key бар екенін тексеру"""
    # Airline алу немесе қосу
    result = await db.execute(select(Airline).where(Airline.name=="Air Astana"))
    air_astana = result.scalar_one_or_none()
    if not air_astana:
        air_astana = Airline(name="Air Astana", country="Kazakhstan")
        db.add(air_astana)
        await db.commit()
        await db.refresh(air_astana)

    result = await db.execute(select(Airline).where(Airline.name=="Fly Arystan"))
    fly_arystan = result.scalar_one_or_none()
    if not fly_arystan:
        fly_arystan = Airline(name="Fly Arystan", country="Kazakhstan")
        db.add(fly_arystan)
        await db.commit()
        await db.refresh(fly_arystan)

    # Debug: базадағы барлық airline-дерді көрсету
    result = await db.execute(select(Airline))
    airlines_in_db = result.scalars().all()
    print("Airlines in DB:", [(a.id, a.name) for a in airlines_in_db])

    # Flight деректері
    flights_data = [
        {"flight_number": "KC101", "destination": "Astana", "airline": air_astana},
        {"flight_number": "FS202", "destination": "Shymkent", "airline": fly_arystan},
    ]

    for f in flights_data:
        # Duplicate тексеру: бір airline + flight_number комбинациясы базаға бар ма
        result = await db.execute(
            select(Flight).where(
                (Flight.flight_number == f["flight_number"]) &
                (Flight.airline_id == f["airline"].id)
            )
        )
        exists = result.scalar_one_or_none()
        if not exists:
            flight = Flight(
                flight_number=f["flight_number"],
                destination=f["destination"],
                airline_id=f["airline"].id  # <- базаға бар UUID
            )
            await db.add(flight)

    await db.commit()

async def run_seeders(db: AsyncSession):
    await seed_airlines(db)
    await seed_flights(db)

async def main():
    async with AsyncSessionLocal() as db:
        await run_seeders(db)

if __name__ == "__main__":
    asyncio.run(main())