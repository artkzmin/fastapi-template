import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


import asyncio
from src.database import engine, BaseOrm


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(BaseOrm.metadata.drop_all)
        await conn.run_sync(BaseOrm.metadata.create_all)


async def init() -> None:
    await init_db()


def main() -> None:
    asyncio.run(init())


if __name__ == "__main__":
    main()
