from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image, ImageFont, ImageDraw
import logging
import urllib.request
import os

TOKEN = '5494085357:AAHmoBoBDZ9ppiHBF1Lxg1gHGV_kcm2KbQw'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

message_list = []
mydir = "images"
def mem(mes, new_image):
    width, height = new_image.size
    font = ImageFont.truetype("arial.ttf", 50)
    pencil = ImageDraw.Draw(new_image)
    w, h = pencil.textsize(mes, font=font)
    pencil.text(((width-w)/2,(height-h)/2), mes, font=font, fill="yellow")
    new_image.save("images/image1.jpg")
    
def image(update, context):
    global message_list
    global image
    str_file = update.message.photo[-1].file_id
    file = context.bot.get_file(str_file)
    path_url_path = file.file_path
    urllib.request.urlretrieve(path_url_path, 'images/image.jpg')
    image = Image.open("images\image.jpg")
    id=update.effective_chat.id
    try:
        mem(message_list[-1], image)
        context.bot.send_photo(chat_id=id,photo=open('images\image1.jpg', 'rb'))
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="вы забыли добавить текст к картинке")
    else:
        message_list = []
        files = os.listdir("images")
        for file in files:
            os.remove(os.path.join(mydir, file))
        image = 0
        

def text(update, context):
    global message_list
    global image
    message = update.message.text
    message_list.append(message)
    id=update.effective_chat.id
    try:
        mem(message_list[-1], image)
        context.bot.send_photo(chat_id=id,photo=open('images\image1.jpg', 'rb'))    
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="загрузите картинку")
    else:
        message_list = []
        files = os.listdir("images")
        for file in files:
            os.remove(os.path.join(mydir, file))  
        image = 0
        

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='введите текст для картинки')

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    text_handler = MessageHandler(Filters.text, text)
    photo_handler = MessageHandler(Filters.photo, image)
    
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(text_handler)
    dispatcher.add_handler(photo_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

