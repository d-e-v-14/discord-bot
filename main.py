import asyncio
import os

from discord.utils import setup_logging
from core import Bot 


load_dotenv()  
token = os.getenv("TOKEN")  

async def main() -> None:
    setup_logging()
 
    async with Bot() as bot: 
        await bot.start(token=token, reconnect=True)

if __name__ == "__main__":
    asyncio.run(main())
