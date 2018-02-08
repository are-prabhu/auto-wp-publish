from utils.config_manager import ConfigManager
config_obj = ConfigManager.get_instance()
config = config_obj.dataMap
from auth import BasicAuth
import urllib.request
import os
import json
import requests
import base64

class ArticlePost(object):
    def __init__(self):
        self.postsurl = config['wp_posts']
        self.reqsesion = requests.session()
        self.basic_auth = BasicAuth.auth

    def postarticle(self,title,description,featurimg,status='publish'):
        header = {
                'Content-Type' : 'application/json',
                'Authorization': 'Basic {basic_auth}'.format(basic_auth=self.basic_auth)
                }
        article = {}
        article['title'] = title
        article['content'] = description 
        article['status'] = status
        article['featured_media'] = featurimg
        article['format'] = 'standard'
        article['author'] = '1'
        article['date'] = '2017-06-19T20:00:35'
       
        article=json.dumps(article)

        postartical = self.reqsesion.post(
            url=self.postsurl, 
            headers=header, 
            data=article,
            auth=(config['wp_username'],config['wp_password'])
            )

        if postartical.status_code == 200:
            return True
        return False
                


