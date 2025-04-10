import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

# Your Telegram Bot Token
API_TOKEN = 8013983070:AAGdnHwfIUV7tr9GwPcrpfF6Ms56zCoYUHI

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Command handler: Start
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.reply("Hello! I am LuxAlgoBot. How can I assist you today?")

# Command handler: Help
@dp.message_handler(commands=['help'])
async def help(msg: types.Message):
    await msg.reply("This bot provides insights based on Lux Algo. Use /start to begin.")

# Default handler for non-command messages
@dp.message_handler()
async def echo(msg: types.Message):
    await msg.reply(f"You said: {msg.text}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
