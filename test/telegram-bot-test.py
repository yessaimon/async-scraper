import asyncio
from aiogram import Bot, Dispatcher, types

from async_scraper import fetch, close

WEATHER_URL = (
    "https://www.accuweather.com/"
    "en/gb/london/ec4a-2/weather-forecast/328328"
)

SELECTOR = "span"


bot = Bot(token='TOKEN')

dp = Dispatcher()


@dp.message()
async def weather(message: types.Message):

    if message.text.lower() in ("погода", "weather"):

        try:
            temperature = await fetch(
                WEATHER_URL,
                SELECTOR
            )

            await message.answer(
                f"Weather: {temperature}"
            )

        except Exception:
            await message.answer(
                "Failed to get weather data"
            )


async def main():

    try:
        await dp.start_polling(bot)

    finally:
        await close()


if __name__ == "__main__":
    asyncio.run(main())

