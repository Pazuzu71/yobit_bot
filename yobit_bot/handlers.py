from config import admin_id

from main import bot, dp, get_price_btc_usd
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Поехали!11")


@dp.message_handler(Text(equals='price'.lower()))
async def send_price(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text='Waiting...')
    await bot.send_message(chat_id=message.from_user.id, text=get_price_btc_usd())


@dp.message_handler(commands='start')
async def start(message: Message):
    start_buttons = ['price']
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await bot.send_message(chat_id=message.from_user.id, text="Нажми на кнопку", reply_markup=keyboard)