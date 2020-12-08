import telegram


def send_message(message, bot):
    return bot.send_message(chat_id=CHAT_ID, text=message)


CHAT_ID = '32989550'  # добавить chat_id
TELEGRAM_TOKEN = '1440023732:AAHl6SURCOrJQfJ4X_Xv56FG-MOUuzNa_oo'  # добавить токен
bot = telegram.Bot(token=TELEGRAM_TOKEN)  # проинициализируйте бота здесь
send_message('hello', bot)
