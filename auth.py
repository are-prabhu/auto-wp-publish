
import base64
from utils.config_manager import ConfigManager
config_obj = ConfigManager.get_instance()
config = config_obj.dataMap

class BasicAuth(object):
    def __init__(self):
        self.wp_host = config['wp_host']
        self.wp_user = config['wp_username']
        self.wp_passwd = config['wp_password']

    def auth(self):
        auth = base64.b64encode('{user}:{passwd}'.format(user=self.wp_user,passwd=self.wp_passwd).encode())
        return str(auth)

