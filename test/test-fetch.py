import asyncio
from async_scraper import fetch, close
site = 'https://example.com/weather'
graduse = 'span'
async def main():
    temperatura = await fetch(
        site,
        graduse
    )
    print(temperatura)
    await close()
asyncio.run(main())
