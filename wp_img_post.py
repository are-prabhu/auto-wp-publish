from utils.config_manager import ConfigManager
config_obj = ConfigManager.get_instance()
from auth import BasicAuth 
import urllib.request
import os
import requests
import base64


class ImagePost(object):
    def __init__(self,imgurl):
        self.imgurl = imgurl
        self.mediaurl = config_obj.wp_mediaurl
        self.reqsesion = requests.session()
        self.basic_auth = BasicAuth.auth

    def is_downloadable(self):
        """
        Does the url contain a downloadable resource
        """
        h = requests.head(self.imgurl, allow_redirects=True)
        header = h.headers
        content_type = header.get('content-type')
        if 'text' in content_type.lower():
            return None
        if 'html' in content_type.lower():
            return None
        return True

    def contenttype(self):
        h = requests.head(self.imgurl, allow_redirects=True)
        header = h.headers
        content_type = header.get('content-type')
        return content_type

    def filename(self):
        """
        Get the file name of the image
        """
        if self.imgurl.find('/'):
            return self.imgurl.rsplit('/', 1)[1]

    def postimg(self):
        """
        Post the downloaded image to wp and get the reference ID
        """
        if is_downloadable == True:                
            pass
        else:
            return None

        """
        Download the image from URL and put it in Downloads
        """
        try:
            urllib.request.urlretrieve(self.imgurl,'%s/downloads/%s' % (os.getcwd(),self.filename()))
        except Exceptation as err:
            print (err)
            return None

        imgread = open('%s/downloads/%s' % (os.getcwd(),self.filename()), 'rb').read()
        header = {
            'Content-Type': self.contenttype(),
            'Authorization': 'Basic {basic_auth}'.format(basic_auth=self.basic_auth)
            'Content-Disposition' : 'attachment; filename=%s' % self.fileName()
        }

        postimgreq = self.reqsesion.post(url=self.mediaurl,
            headers = header, data = imgread )

        if postimgreq.status_code == 201:
            os.remove('%s/downloads/%s' % (os.getcwd(),self.filename))
            return json.loads(postimgreq.text)['id']
        else:
            return None

