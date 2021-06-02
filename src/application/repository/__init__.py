import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

class Repostory:
    def __init__(self):
        self.engine: AIOEngine = None


repository = Repostory()


async def connect_db():
    """Create database connection."""
    client = AsyncIOMotorClient("mongodb://localhost:27017/")
    engine = AIOEngine(motor_client=client, database="testtt")
    repository.engine = engine

