from config import token

import requests
from aiogram import Bot, Dispatcher, executor
import asyncio


def get_price_btc_usd():
    API_url = "https://yobit.net/api/3/ticker/btc_usd"
    req = requests.get(API_url).json()
    price = req['btc_usd']['sell']
    # print(price)
    return price


bot = Bot(token, parse_mode="HTML")
dp = Dispatcher(bot=bot)


if __name__ == "__main__":
    # print(get_price_btc_usd())
    from handlers import send_to_admin
    from handlers import bot, dp
    executor.start_polling(dp, on_startup=send_to_admin)