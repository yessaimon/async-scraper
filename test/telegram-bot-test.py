from async_scraper import fetch, close
from aiogram import Bot, Dispatcher, types
import asyncio


url = "https://www.accuweather.com/ru/kg/bosteri/226688/weather-forecast/226688"
selector = ".temp"


bot = Bot(token="TOKEN")
dp = Dispatcher()


@dp.message()
async def weather(msg: types.Message):

    if msg.text.lower() == "погода":

        temp = await fetch(
            url,
            selector
        )

        await msg.answer(
            f"🌡 Температура: {temp}"
        )


async def main():

    try:
        await dp.start_polling(bot)

    finally:
        await close()
asyncio.run(main())
