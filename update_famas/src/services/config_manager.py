import json
from models.constants import Paths
class ConfigManager():

    def __init__(self):
        self.config_path = Paths.CONFIG
        self.data = self.load(self.config_path)

    def load(self, path: str) -> dict:
        with open(path, "r") as f:
            data = json.load(f)
        return data

    def save(self, path: str, data: dict):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
    def get(self,key):
        return self.data.get(key)
            
    def update_config(self, key : str, value : any):
            data = self.load(self.config_path)
            data[key] = value
            self.save(self.config_path, data)
    
    