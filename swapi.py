import urllib.parse
import requests
from utils import Utils
from config import config
import json

from resources import Resource, Film, Person

class swapi:

    @staticmethod
    def get_films():
        pass

    @staticmethod
    def get_characters():
        pass
    
if __name__ == "__main__":
    print("What star wars actually is: ")
    for i in range(1, 4):
        print("\t -> ", swapi.get_films(i))

    uno = swapi.get_films(1)
    for p in uno.characters:
        print(p)
        
        