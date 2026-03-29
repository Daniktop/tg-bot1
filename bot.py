import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = os.getenv("8498298692:AAEnYgsoJ4MhkSbsjdZiR5fFLXycz5J2l7o")  # или вставь строкой

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("👋 Привет! Я тестовый бот.")

# Команда /balance
@dp.message(Command("balance"))
async def balance(message: Message):
    await message.answer("💰 Твой баланс: 1000$")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())