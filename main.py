from telegram.ext import ApplicationBuilder, CommandHandler

from bot import start, lisa, tehtud, statistika, list_habits, eemalda

TOKEN="8600857881:AAFzeOATahpJC5ZzwXVOYwj-AaBhP1l7k2o"

def main():
    app=ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("lisa", lisa))
    app.add_handler(CommandHandler("tehtud", tehtud))
    app.add_handler(CommandHandler("statistika", statistika))
    app.add_handler(CommandHandler("list", list_habits))
    app.add_handler(CommandHandler("eemalda", eemalda))

    print("Bot töötab...")
    app.run_polling()

if __name__ == "__main__":
    main()
