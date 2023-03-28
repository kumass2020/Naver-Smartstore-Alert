import requests
from bs4 import BeautifulSoup
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import threading

url = 'url'
message = 'message'
telegram_token = 'token'
telegram_chat_id = 0000000000

bot = telegram.Bot(token=telegram_token)


def parse():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    element = soup.select('#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._2BQ-WF2QUb > strong1')
    if len(element) == 0:
        print('no Product!')
        pass
    else:
        bot.sendMessage(chat_id=telegram_chat_id, text=message)

    threading.Timer(60, parse).start()


if __name__ == '__main__':
    parse()
