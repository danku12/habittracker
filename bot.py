from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from andmed import lae_andmed, salvesta_andmed
from statistika import kuva_statistika

andmed = lae_andmed()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start käsk."""
    await update.message.reply_text("Tere! See on harjumuste jälgimise bot.")


async def lisa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Lisa uus harjumus."""
    kasutaja = str(update.effective_user.id)
    nimi=" ".join(context.args)

    if not nimi:
        await update.message.reply_text("Kasuta: /lisa harjumuse_nimi")
        return

    if kasutaja not in andmed:
        andmed[kasutaja]={}

    if nimi in andmed[kasutaja]:
        await update.message.reply_text("See harjumus on juba olemas.")
        return

    andmed[kasutaja][nimi]=0
    salvesta_andmed(andmed)

    await update.message.reply_text(f"Harjumus '{nimi}' lisatud!")


async def tehtud(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Lisa kogus (nt ml, km jne)."""
    kasutaja = str(update.effective_user.id)

    try:
        nimi=context.args[0]
        kogus=int(context.args[1])
    except:
        await update.message.reply_text("Kasuta: /tehtud nimi kogus")
        return

    if nimi in andmed.get(kasutaja, {}):
        andmed[kasutaja][nimi]+=kogus
        salvesta_andmed(andmed)

        await update.message.reply_text(f"Lisatud {kogus} ✅")
    else:
        await update.message.reply_text("Sellist harjumust ei ole.")


async def statistika(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("STATISTIKA WORKS")
    kasutaja = str(update.effective_user.id)

    if kasutaja in andmed:
        text=kuva_statistika(andmed[kasutaja])
    else:
        text="Pole andmeid."

    await update.message.reply_text(text)
    
async def list_habits(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Näita kõiki harjumusi."""
    kasutaja = str(update.effective_user.id)

    if kasutaja not in andmed or not andmed[kasutaja]:
        await update.message.reply_text("Sul pole veel harjumusi.")
        return

    text="Sinu harjumused:\n\n"

    for nimi in andmed[kasutaja]:
        text+=f"• {nimi}\n"

    await update.message.reply_text(text)

async def eemalda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Eemalda harjumus."""
    kasutaja=str(update.effective_user.id)
    nimi=" ".join(context.args)

    if not nimi:
        await update.message.reply_text("Kasuta: /eemalda harjumuse_nimi")
        return

    if nimi in andmed.get(kasutaja, {}):
        del andmed[kasutaja][nimi]
        salvesta_andmed(andmed)
        await update.message.reply_text(f"Harjumus '{nimi}' eemaldatud.")
    else:
        await update.message.reply_text("Sellist harjumust ei ole.")
