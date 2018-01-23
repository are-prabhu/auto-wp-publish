from utils.config_manager import ConfigManager
config_obj = ConfigManager.get_instance()
from auth import BasicAuth
import urllib.request
import os
import requests
import base64

class ArticalPost(object):
    def __init__(self,title,description,featurimg,status='publish'):
        self.postsurl = config_obj.wp_posts
        self.status = status
        self.featurimg = featurimg
        self.title = title
        self.description = description
        self.basic_auth = BasicAuth.auth
        self.reqsesion = requests.session()

    def poster(self):
        header = {
                'Content-Type' : 'application/json',
                'Authorization': 'Basic {basic_auth}'.format(basic_auth=basic_auth)
                }
        article = {}
        article['title'] = self.title
        article['content'] = self.description 
        article['status'] = self.status
        article['featured_media'] = self.featurimg
       
        print(article)
        postartical = self.reqsesion.post(url=self.postsurl, headers=header, data=article)
        


