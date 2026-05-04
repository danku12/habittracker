from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from andmed import lae_andmed, salvesta_andmed
from statistika import kuva_statistika

andmed = lae_andmed()                        # загружаем данные при старте бота


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tere! See on harjumuste jälgimise bot.")
    # приветственное сообщение


async def lisa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kasutaja = str(update.effective_user.id)    # получаем id пользователя
    nimi = " ".join(context.args)               # берём название привычки из команды

    if not nimi:
        await update.message.reply_text("Kasuta: /lisa harjumuse_nimi")
        return                                  # если название не ввели

    if kasutaja not in andmed:
        andmed[kasutaja] = {}                   # создаём словарь для нового юзера

    if nimi in andmed[kasutaja]:
        await update.message.reply_text("See harjumus on juba olemas.")
        return                                  # если привычка уже есть

    andmed[kasutaja][nimi] = 0                  # добавляем привычку с 0
    salvesta_andmed(andmed)                     # сохраняем

    await update.message.reply_text(f"Harjumus '{nimi}' lisatud!")


async def tehtud(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kasutaja = str(update.effective_user.id)    # id пользователя

    try:
        nimi = context.args[0]                  # название привычки
        kogus = int(context.args[1])            # сколько добавить
    except:
        await update.message.reply_text("Kasuta: /tehtud nimi kogus")
        return                                  # если формат команды неверный

    if nimi in andmed.get(kasutaja, {}):
        andmed[kasutaja][nimi] += kogus         # прибавляем прогресс
        salvesta_andmed(andmed)                 # сохраняем

        await update.message.reply_text(f"Lisatud {kogus} ✅")
    else:
        await update.message.reply_text("Sellist harjumust ei ole.")


async def statistika(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kasutaja = str(update.effective_user.id)    # id пользователя

    if kasutaja in andmed:
        text = kuva_statistika(andmed[kasutaja])  # создаём статистику
    else:
        text = "Pole andmeid."                    # если данных нет

    await update.message.reply_text(text)


async def list_habits(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kasutaja = str(update.effective_user.id)      # id пользователя

    if kasutaja not in andmed or not andmed[kasutaja]:
        await update.message.reply_text("Sul pole veel harjumusi.")
        return                                    # если привычек нет

    text = "Sinu harjumused:\n\n"

    for nimi in andmed[kasutaja]:
        text += f"• {nimi}\n"                     # добавляем все привычки в список

    await update.message.reply_text(text)


async def eemalda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kasutaja = str(update.effective_user.id)      # id пользователя
    nimi = " ".join(context.args)                 # название привычки

    if not nimi:
        await update.message.reply_text("Kasuta: /eemalda harjumuse_nimi")
        return

    if nimi in andmed.get(kasutaja, {}):
        del andmed[kasutaja][nimi]                # удаляем привычку
        salvesta_andmed(andmed)                   # сохраняем
        await update.message.reply_text(f"Harjumus '{nimi}' eemaldatud.")
    else:
        await update.message.reply_text("Sellist harjumust ei ole.")
