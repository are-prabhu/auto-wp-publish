from newspaper import Article
import nltk
nltk.download('punkt')

class Scraper:
    """
    Scraper is to strip article of a given URL and returns images, description, title, pub date. 
    TODO: find better logic to remove nasty if loops 
    """
    @classmethod
    def article(cls,url,description):
        article = Article(url)
        article.download()
        article.parse()
        url_insight={}
        url_insight['title']=article.title
        url_insight['top_image']=article.top_image
        url_insight['description']=(article.summary)


        if not article.title:
            url_insight['title']=None
        if not article.top_image:
            url_insight['top_image']=None

        url_insight['description']=(article.text)
        return url_insight


#Scraper.article('http://opensourceforu.com/2016/07/22843/',True)
#scraper.article('http://www.bbc.com/news/av/world-asia-43158243/world-s-longest-glass-bridge-visited-by-thousands-daily')
#Scraper.article('https://www.cloudyn.com/blog/how-to-estimate-ebs-snapshot-backup-costs/',True)

        
