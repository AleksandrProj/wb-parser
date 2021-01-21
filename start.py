from bot.core import WildberriesBot

bot = WildberriesBot()


if __name__ == '__main__':
    try:
        bot.run()
    except KeyboardInterrupt:
        bot.close()