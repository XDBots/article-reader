from newspaper import Article


def getArticleContent(url): 
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
            short_title = title[:16]
            tts = gTTS(title +"."+ content)
            tts.save(short_title + ".mp3")
            return True
        except: 
            print("try again...")
            return False
