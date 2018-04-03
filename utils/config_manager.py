import yaml
import os
from gevent import lock

class Config():
    def __init__(self, fname="config.yaml"):
        self.load(fname)

    def load(self, fname):
        self.def_home_dir = os.environ.get("OBD_HOME_DIR", os.getcwd())
        default = os.path.join(self.def_home_dir, "config", fname)

        self.config = os.environ.get("OBD_CONFIG", default)
        self.dataMap = yaml.load(open(self.config))

    def dump(self):
        print(self.dataMap)

class ConfigManager(object):
    config_obj = None
    _lock = lock.RLock()

    @classmethod
    def get_instance(cls, fname="config.yaml"):
        if not cls.config_obj:
            with cls._lock:
                if not cls.config_obj:
                    cls.config_obj = Config(fname)
        return cls.config_obj


