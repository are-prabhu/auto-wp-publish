from utils.config_manager import ConfigManager
config_obj = ConfigManager.get_instance()
from wp_actions.wp_artical_post import ArticlePost
from wp_actions.wp_img_post import ImagePost
from web_scrapers.newscraper import Scraper


class Posters(object):
    def __init__(self,url,categorie,status,description):
        self.url = url
        self.categorie = categorie
        self.status=status
        self.scrape = Scraper.article(self.url,description)

    def post(self):
        imgid=ImagePost().postimg(self.scrape['top_image'])
        return ArticlePost().postarticle(self.scrape['title'],self.categorie,self.status,self.scrape['description'],imgid,self.url)

#Posters('http://www.bbc.com/news/av/world-asia-43158243/world-s-longest-glass-bridge-visited-by-thousands-daily','7').post()
#test=Posters('http://opensourceforu.com/2016/07/22843/','5','publish',True).post()
#print ('***************')
#print(test)
#Posters('https://fashionista.com/2015/02/most-influential-style-bloggers-2015','6').post()
#Posters('https://codeburst.io/building-an-api-with-django-rest-framework-and-class-based-views-75b369b30396', '5').post()
