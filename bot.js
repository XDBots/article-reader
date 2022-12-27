require('dotenv').config()

const gTTS = require("gtts")
const { Bot } = require("grammy");
const { InputFile } = require("grammy");

const isValidURL = require("./utils/url_validator")

const BOT_TOKEN = process.env.BOT_TOKEN;



const bot = new Bot(BOT_TOKEN);

bot.command("start", (ctx) => {
    ctx.reply("Hi, Thanks for starting me :)", {
      reply_to_message_id: ctx.msg.message_id,
    });
  });


bot.command("tts",(ctx)=> {
    const msg = ctx.msg.text;
    //console.log(msg);
    if (msg=="/tts"){
        ctx.reply("Please enter a website url!");
        
    }
    else{
        const url = msg.slice(5);
        console.log(url);
        if (isValidURL(url)== true){
            ctx.reply("Processing... might take sometime", {
                reply_to_message_id: ctx.msg.message_id,
              });


            //HANDLE THE TEXT
                
            const Build = require('newspaperjs').Build;
            const Article = require('newspaperjs').Article;


            Article(url)
            .then(result=>{
                const title = result.title;
                const text = result.text;
                const wholeText = title + ".\n " + text;
                //console.log(wholeText);
                console.log('content scraped');


                const gtts = new gTTS(wholeText, 'en');
                const fileName = "audio" + ".mp3";
                //TTS
                gtts.save(fileName, function () {
                    console.log('Success! TTS...');
                    ctx.replyWithAudio(new InputFile(fileName), {
                    title: title,
                    performer : "Article Reader"
                    });
                    console.log("audio is being sent...");
                    

                });
                })
            .catch(reason=>{
                //return false
                console.log(reason);
                ctx.reply(reason);
                });

        
        }
        
    
    }

})


bot.start();