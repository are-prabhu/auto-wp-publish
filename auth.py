
import base64
from utils.config_manager import ConfigManager
config_obj = ConfigManager.get_instance()

class BasicAuth(object):
    def __init__(self):
        self.wp_host = config_obj.wp_host
        self.wp_user = config_obj.wp_username
        self.wp_passwd = config_obj.wp_password

    def auth(self):
        auth = base64.b64encode('{user}:{passwd}'.format(user=self.wp_user,passwd=self.wp_passwd).encode())
        return str(auth)
