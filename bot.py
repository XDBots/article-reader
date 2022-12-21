from decouple import config

import telebot

import os

from scraper import getArticleContent, tts
from url_validator import isValidURL

BOT_TOKEN = config("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "I am your article reader bot.")

#Handle '/tts'
@bot.message_handler(commands=['tts'])
def echo_message(message):
    url = message.text
    modified_url = isValidURL(url)
    
    if modified_url == False:
        bot.reply_to(message, "Provide a website URL.")
        
    else:
        link = modified_url[0]
        print(link)
        bot.reply_to(message, "Ok, Processing...")
        title , content = getArticleContent(link)
        print("scraping complete")

        result = tts(title, content)
        
        if result == True:

            chat_id = message.chat.id
            short_title = title[:16]

            audio = open(short_title + '.mp3', 'rb')
            #bot.send_audio(chat_id, audio)
            bot.send_audio(chat_id, audio,  performer='Article Reader', title=title)
            print("Sent successfully")
            audio.close()
            if True:
                os.remove(short_title + ".mp3")
            
        else:
            bot.reply_to(message, "Sorry, Can't Process this Article")


bot.infinity_polling()
