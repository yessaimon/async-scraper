import asyncio
from async_scraper import fetch, close
site = 'https://www.accuweather.com/ru/kg/bosteri/226688/weather-forecast/226688'
graduse = 'span'
async def main():
    temperatura = await fetch(
        site,
        graduse
    )
    print(temperatura)
    await close()
asyncio.run(main())
