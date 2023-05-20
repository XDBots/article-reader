from decouple import config

import telebot

import os

from scraper import getArticleContent, tts
from url_validator import isValidURL

BOT_TOKEN = config("BOT_TOKEN")
if BOT_TOKEN is None:
    print("Enter Your Bot Token in .env file.")
bot = telebot.TeleBot(BOT_TOKEN)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "I am your article reader bot.")

#Handle '/tts'
@bot.message_handler(commands=['tts'])
def textToSpeech(message):
    url = message.text
    modified_url = isValidURL(url)
    
    if modified_url == False:
        bot.reply_to(message, "Provide a website URL.")
        
    else:
        link = modified_url[0]
        print(link)
        bot.reply_to(message, "Ok, Processing...it might take sometime")
        wholeText = getArticleContent(link)
        if wholeText is not None:
            title, content = wholeText
            print("scraping complete")
            result = tts(title, content)
        
            if result == True:

                chat_id = message.chat.id
                

                audio = open("audio.mp3", 'rb')
                #bot.send_audio(chat_id, audio)
                bot.send_audio(chat_id, audio,  performer='Article Reader', title=title)
                print("Sent successfully")
                audio.close()
                if True:
                    os.remove("audio.mp3")
            else:
                bot.reply_to(message, "Sorry, failure converting text to audio")
            
        else:
            bot.reply_to(message, "Sorry, Can't Process this Article")


bot.polling()
