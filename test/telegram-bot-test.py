from async_scraper import fetch,close
from aiogram import Bot,Dispatcher,types
import asyncio
url = 'https://www.accuweather.com/en/gb/london/ec4a-2/weather-forecast/328328'
graduce = 'span'
bot = Bot(token='confidential information')
dp = Dispatcher()
@dp.message()
async def mainp(msg : types.Message):
	if msg.text.lower() == 'weather' or 'погода':
		tmp = await fetch(url,graduce)
		await close()
		await msg.answer(f'weather: {tmp}')
async def main():
	await dp.start_polling(bot)
asyncio.run(main())
