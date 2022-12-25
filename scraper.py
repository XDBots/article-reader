from newspaper import Article
from decouple import config

HTTP_PROXY = config("HTTP_PROXY")
HTTPS_PROXY = config("HTTPS_PROXY")


def getArticleContent(url):
    try:
        article = Article(url)
        article.download()
    except Exception as e:
        print(e)
        if HTTP_PROXY != None and HTTPS_PROXY != None:
            try:
                article = Article(url, proxies={
                    "http": HTTP_PROXY,
                    "https": HTTPS_PROXY })
                article.download()
            except Exception as e:
                return None
        else:
            return None

    article.parse()
    title = article.title
    content = article.text
    return title, content
        
        


from gtts import gTTS
def tts(title, content):
        try:
            tts = gTTS(title +"."+ content)
            tts.save("audio.mp3")
            return True
        except: 
            print("try again...TTS")
            return False
