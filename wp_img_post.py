from utils.config_manager import ConfigManager
config_obj = ConfigManager.get_instance()
config = config_obj.dataMap
from auth import BasicAuth 
import urllib.request
import json
import os
import requests
import base64

class ImagePost(object):
    def __init__(self):
        self.mediaurl = config['wp_mediaurl']
        self.reqsesion = requests.session()
        self.basic_auth = BasicAuth.auth

    def is_downloadable(self,imgurl):
        """
        Does the url contain a downloadable resource
        """
        h = requests.head(imgurl, allow_redirects=True)
        header = h.headers
        content_type = header.get('content-type')
        if 'text' in content_type.lower():
            return None
        if 'html' in content_type.lower():
            return None
        return True

    def contenttype(self,imgurl):
        h = requests.head(imgurl, allow_redirects=True)
        header = h.headers
        content_type = header.get('content-type')
        return content_type

    def filename(self,imgurl):
        """
        Get the file name of the image
        """
        if imgurl.find('/'):
            return imgurl.rsplit('/', 1)[1]

    def postimg(self,imgurl):
        """
        Post the downloaded image to wp and get the reference ID
        """
        if self.is_downloadable(imgurl) == True:                
            pass
        else:
            return None

        """
        Download the image from URL and put it in Downloads
        """
        try:
            urllib.request.urlretrieve(imgurl,'%s/downloads/%s' % (os.getcwd(),self.filename(imgurl)))
        except Exceptation as err:
            print (err)
            return None

        imgread = open('%s/downloads/%s' % (os.getcwd(),self.filename(imgurl)), 'rb').read()
        
        header = {
            'Content-Type': self.contenttype(imgurl),
            'Authorization': 'Basic {basic_auth}'.format(basic_auth=self.basic_auth),
            'Content-Disposition' : 'attachment; filename=%s' % self.filename(imgurl)
        }

        postimgreq = self.reqsesion.post(
            url=self.mediaurl,
            headers = header, 
            data = imgread, 
            auth=(config['wp_username'],config['wp_password'])
        )

        print(postimgreq.status_code)         
       
        if postimgreq.status_code == 201:
            os.remove('%s/downloads/%s' % (os.getcwd(),self.filename(imgurl)))
            return json.loads(postimgreq.text)['id']
        else:
            return None


