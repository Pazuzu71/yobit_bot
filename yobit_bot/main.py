import requests


def get_price_btc_usd():
    API_url = "https://yobit.net/api/3/ticker/btc_usd"
    req = requests.get(API_url).json()
    price = req['btc_usd']['sell']
    # print(price)
    return price


if __name__ == "__main__":
    print(get_price_btc_usd())