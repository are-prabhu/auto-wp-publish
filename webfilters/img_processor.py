from utils.config_manager import ConfigManager
config_obj = ConfigManager.get_instance()
from wp_artical_post import ArticlePost
from wp_img_post import ImagePost
from scraper import ArticleURL


class Posters(object):
    def __init__(self,url,categorie):
        self.url = url
        self.categorie = categorie
        self.scrape = ArticleURL(self.url)
        print(self.scrape)

    def post(self):
        imgid=ImagePost().postimg(self.scrape['thumbnail'])
        return ArticlePost().postarticle(self.scrape['title'],self.categorie,self.scrape['description'],imgid,self.url)

#Posters('http://www.bbc.com/news/world-middle-east-42412729','1').post()
