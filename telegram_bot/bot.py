import os
from telegram.ext import Updater, CommandHandler, MessageHandler

token = os.getenv('TELEGRAM_BOT_TOKEN')

# Define la función que maneja el comando de inicio
def start(update, context):
    update.message.reply_text('Hola! Envíame un archivo de audio para procesarlo.')

# Define la función que maneja los archivos de audio
def handle_audio(update, context):
    # Descarga el archivo de audio
    file = context.bot.get_file(update.message.voice.file_id)
    file.download('audio.ogg')
    
    # Realiza cualquier acción que desees con el archivo de audio
    # En este ejemplo, simplemente lo renombramos
    os.rename('audio.ogg', 'audio_recibido.ogg')
    
    # Envía una respuesta al usuario
    update.message.reply_text('Archivo de audio recibido y procesado correctamente.')

# Crea un nuevo bot
updater = Updater('TOKEN', use_context=True)

# Agrega un manejador para el comando de inicio
updater.dispatcher.add_handler(CommandHandler('start', start))

# # Agrega un manejador para los archivos de audio
# updater.dispatcher.add_handler(MessageHandler(Filters.voice, handle_audio))

# Inicia el bot
updater.start_polling()
updater.idle()
