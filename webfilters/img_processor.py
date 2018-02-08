from utils.config_manager import ConfigManager
config_obj = ConfigManager.get_instance()
from wp_artical_post import ArticlePost
from wp_img_post import ImagePost
from scraper import ArticleURL

#art=ArticleURL('http://www.bbc.com/news/world-middle-east-42412729')

class Posters(object):
    def __init__(self,url):
        self.url = url
        self.scrape = ArticleURL(self.url)

    def post(self):
        imgid=ImagePost().postimg(self.scrape['thumbnail'])
        return ArticlePost().postarticle(self.scrape['title'],self.scrape['description'],imgid)

#Posters('http://www.bbc.com/news/world-middle-east-42412729').post()
