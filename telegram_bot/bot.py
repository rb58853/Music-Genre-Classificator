import telebot
import os
import model

TOKEN = '6152621847:AAE0zasatsZxif2nTV1BsxN_mkBKpmx45Ng'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenido, ¿en qué puedo ayudarte?")

@bot.message_handler(content_types=['voice', 'audio'])
def handle_audio(message):
    if message.content_type == 'voice':
        file_info = bot.get_file(message.voice.file_id)
    elif message.content_type == 'audio':
        file_info = bot.get_file(message.audio.file_id)
    else:
        return

    downloaded_file = bot.download_file(file_info.file_path)
    path_name = 'random_name'
    with open(path_name, 'wb') as fd:
        fd.write(downloaded_file)
    # Envía un mensaje al usuario que envió el audio
    bot.send_message(message.chat.id, "He recibido tu audio. Lo clasificare en un genero musical. Estoy entrenado para diferenciar entre los posibles generos:\n⦿ <code>blues</code> \n⦿ <code>classical</code> \n⦿ <code>country</code> \n⦿ <code>disco</code>\n⦿ <code>hiphop</code> \n⦿ <code>jazz</code>, \n⦿ <code>metal</code>, \n⦿ <code>pop</code>, \n⦿ <code>reggae</code>, \n⦿ <code>rock</code>", parse_mode='html')
    genre = model.get_genre(path_name)
    bot.send_message(message.chat.id, f"El genero de su audio es <code>{genre}</code>.", parse_mode= 'html')



bot.polling(none_stop=True)
