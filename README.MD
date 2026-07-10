честно,я сделал чисто для себя но он очень полезным оказался,пример кода

Honestly, I made it just for myself, but it turned out to be very useful, here's a code example.
"""
import asyncio
from async_scraper import fetch, close
site = 'конфедициальная информация'
graduse = 'span'
async def main():
    temperatura = await fetch(
        site,
        graduse
    )
    print(temperatura)
    await close()
asyncio.run(main())

"""
и оно выведет типо градус или еще чето,можно крч h1,h2,h3,h4,h5,span,вобщем хтмл теги все
