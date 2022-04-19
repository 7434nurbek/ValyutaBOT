import logging
import requests
from aiogram.dispatcher.filters import Text

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5326241519:AAEt8CvZd7MNpXRJv_OajdkGGVGxCP3eLF4'
API_KEY = '9e0fe90cbd260b947f1311d3'

currentcy = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currentcy}/UZS"
response = requests.get(url)
kurs = f"Bugungi kunda dollar kursi:{response.json()['conversion_rate']}"


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu Alaykum bu bot\nO`zbekiston so`mining \ndollar yoki evroga nisbatan qiymatini \nko'rsatadi.")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#    button_1 = types.KeyboardButton(text="1 USD (dollar)")
#    keyboard.add(button_1)
#    button_2 = "1 ERO (yevro)"
    buttons = ["1 USD (dollar)","1 EUR (yevro)"]
    keyboard.add(*buttons)
    await message.answer("Qaysi valyuta kursini tanlaysiz?", reply_markup=keyboard)

@dp.message_handler(Text(equals="1 USD (dollar)"))
async def with_puree(message: types.Message):
    await message.reply(kurs)

@dp.message_handler(lambda message: message.text == "1 EUR (yevro)")
async def without_puree(message: types.Message):
    currentcy = 'EUR'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currentcy}/UZS"
    response = requests.get(url)
    kurs = f"Bugungi kunda yevro kursi:{response.json()['conversion_rate']}"
    await message.reply(kurs)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
