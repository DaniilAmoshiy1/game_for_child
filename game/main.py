import asyncio
from window import run_game


async def main():
    await run_game()

if __name__ == '__main__':
    asyncio.run(main())
