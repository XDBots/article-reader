from newspaper import Article
from decouple import config

HTTP_PROXY = config("HTTP_PROXY")
HTTPS_PROXY = config("HTTPS_PROXY")


def getArticleContent(url):
    if HTTP_PROXY is not None and HTTPS_PROXY is not None:
        article = Article(url, proxies={
            "http": HTTP_PROXY,
            "https": HTTPS_PROXY })

    article = Article(url)
    article.download()
    article.parse()
    title = article.title
    content = article.text
    return title, content


from gtts import gTTS
def tts(title, content):
    if True:
        try:
            tts = gTTS(title +"."+ content)
            tts.save("audio.mp3")
            return True
        except: 
            print("try again...")
            return False
