from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

TOKEN = '5309893372:AAGkDQzf6ik5lBNJbNJ7QuL6TCXVSBihoBk'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

"""
def echo(update, context):
    # добавим в начало полученного сообщения строку 'ECHO: '
    text = 'ECHO: ' + update.message.text 
    # `update.effective_chat.id` - определяем `id` чата, 
    # откуда прилетело сообщение 
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
"""

def image(update, context):
    context.bot.send_document(chat_id=update.effective_chat.id, document=update.message.document)

def remember_message(update, context):
    message = update.message.text
    error_code = False
    messages = message.split(' ', 1)
    if len(messages) != 1:
        error_code = True
        messages = messages[1]
    return error_code, messages

def echo(update, context):
    error_code, message = remember_message(update ,context)
    if error_code:
        context.bot.send_message(chat_id=update.effective_chat.id, text="вы добавили текст для картинки")
        return message
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="вы забыли добавить текст для картинки")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', echo)
    image_handler = MessageHandler(Filters.document.category("image"), image)
    dispatcher.add_handler(start_handler)
    """
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    """
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

'''
import telebot

TOKEN = '5309893372:AAGkDQzf6ik5lBNJbNJ7QuL6TCXVSBihoBk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'текст для картинки')
    

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'запомнил текст')
    

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src='C:/my_project/bots/first_bot/images/' +file_info.file_path;
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.reply_to(message,"Фото добавлено") 
    except Exception as e:
        bot.reply_to(message,e )


# RUN
#bot.polling(none_stop=True)
if __name__ == '__main__':
  bot.polling(none_stop=True)
'''
