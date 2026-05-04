
from telegram.ext import ApplicationBuilder, CommandHandler

from bot import start, lisa, tehtud, statistika, list_habits, eemalda

TOKEN = "8600857881:AAFzeOATahpJC5ZzwXVOYwj-aABhP1l7k2o"                         # токен бота


def main():
    app = ApplicationBuilder().token(TOKEN).build()   # создаём приложение бота

    app.add_handler(CommandHandler("start", start))         # /start
    app.add_handler(CommandHandler("lisa", lisa))           # /lisa
    app.add_handler(CommandHandler("tehtud", tehtud))       # /tehtud
    app.add_handler(CommandHandler("statistika", statistika)) # /statistika
    app.add_handler(CommandHandler("list", list_habits))    # /list
    app.add_handler(CommandHandler("eemalda", eemalda))     # /eemalda

    print("Bot töötab...")                    # сообщение в консоль
    app.run_polling()                         # запускаем бота


if __name__ == "__main__":
    main()                                    # запуск программы
