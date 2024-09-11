import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '6979608021:AAELjupZdkYegQFBjZCtyLQfZgBhPaFfP_E'
DJANGO_API_URL = "http://django:8000/api/tasks/"
FASTAPI_API_URL = "http://fastapi:8001/comments/"
JWT_TOKEN = None  # Получение токена будет автоматическим

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to the ToDo bot!")

@dp.message_handler(commands=['tasks'])
async def list_tasks(message: types.Message):
    global JWT_TOKEN
    response = requests.get(DJANGO_API_URL, headers={"Authorization": f"Bearer {JWT_TOKEN}"})
    tasks = response.json()
    await message.reply(f"Your tasks: {tasks}")

@dp.message_handler(commands=['comments'])
async def list_comments(message: types.Message):
    global JWT_TOKEN
    response = requests.get(FASTAPI_API_URL, headers={"Authorization": f"Bearer {JWT_TOKEN}"})
    comments = response.json()
    await message.reply(f"Task comments: {comments}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
