import telegram
import os

bot = telegram.Bot(token='1936238104:AAGBNmzFpVWkxqRGGOPeIk1rMMpkIIB4TY4')

def ppomppu():
    bot.sendMessage(1840767554, '테스트')

if __name__ == '__main__':

    try:
        ppomppu()
    except AttributeError as e:
        print(e)