import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Funzione per il comando /start
def start(update: Update, context: CallbackContext) -> None:
    # URL di un'immagine di un cane
    dog_image_url = "https://example.com/dog.jpg"
    keyboard = [[InlineKeyboardButton("Clicca per vedere un cane", url=dog_image_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Clicca qui per vedere un cane!', reply_markup=reply_markup)

def main() -> None:
    # Recupera il token dalla variabile d'ambiente
    TOKEN = os.getenv('TOKEN')

    # Crea l'updater
    updater = Updater(TOKEN)

    # Ottieni il dispatcher per gestire i comandi
    dispatcher = updater.dispatcher

    # Aggiungi un handler per il comando /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Avvia il bot
    updater.start_polling()

    # Mantieni il bot attivo
    updater.idle()

if __name__ == '__main__':
    main()
