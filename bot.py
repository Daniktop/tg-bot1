import asyncio
import os
import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = os.getenv("8498298692:AAEnYgsoJ4MhkSbsjdZiR5fFLXycz5J2l7o")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("🚀 Бот работает на Render!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())