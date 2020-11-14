import urllib.parse
import requests
from utils import Utils
from config import config
import json
from resources import *

class swapi:

    @staticmethod
    def load(attribute, key):
        # TODO parse urls into references
        q = swapi.construct_query(attribute, key)
        return requests.get(q).json()
        
    @staticmethod
    def get_dirty(url):
        return requests.get(url).json()
        
    @staticmethod
    def construct_query(attribute, key):
        if key == None:
            q = f"{config['api-url']}/{attribute}/"
            # raise Exception("Multiple resources not implemented yet")
        elif Utils.is_int_someway(key):
            # is_int_someway checks if is int or its str and a digit
            q = f"{config['api-url']}/{attribute}/{key}"
        else:
            # it's a string 
            pass   

        return q


    @staticmethod
    def GetFilms(key):
        film_dict = swapi.load('films', key)
        if 'detail' in film_dict:
            # if film_dict['detail'] == 'Not found':
            return None


        # deserialize a JSON string
        return Film(**film_dict)

        
    @staticmethod
    def GetCharacters(key):
        pass
    
if __name__ == "__main__":
    print("What star wars actually is: ")
    for i in range(1, 4):
        print("\t -> ", swapi.GetFilms(i))