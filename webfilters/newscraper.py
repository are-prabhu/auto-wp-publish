from newspaper import Article
import nltk
nltk.download('punkt')

class scraper:
    @classmethod
    def article(cls,url):
        article = Article(url)
        article.download()
        article.parse()
        url_insight={}
        url_insight['title']=article.title
        url_insight['top_image']=article.top_image
        url_insight['publish_date']=article.publish_date
        url_insight['description']=article.summary

        if not article.title:
            url_insight['title']=None
        if not article.top_image:
            url_insight['top_image']=None
        if not article.publish_date:
            url_insight['publish_date']=None

        if (len((article.text).split(' ')) < 250 and len((article.text).split(' ')) > 150 ) and article.text:
            url_insight['description']=article.text
        elif (len((article.summary).split(' ')) < 250 and len((article.summary).split(' ')) > 150) and article.summary:
            url_insight['description']=article.summary
        elif article.text:
            url_insight['description'] = ''.join((article.text).strip(' ')[0:250])
        elif article.summary:
            url_insight['description'] = ''.join((article.summary).strip(' ')[0:250])
        print (url_insight)
        return url_insight


#scraper.article('http://opensourceforu.com/2016/07/22843/')
#scraper.article('http://www.bbc.com/news/av/world-asia-43158243/world-s-longest-glass-bridge-visited-by-thousands-daily')

        
