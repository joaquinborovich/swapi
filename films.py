# from resource_abstract_class import Resource
import urllib.parse
import requests
from utils import Utils
from config import config
import json

class Films():
        
    # def __init__(self, title, episode_id, opening_crawl, director, producers, release_date, characters, planets, starships, vehicles, species, url):
    #     self.title = title
    #     self.episode_id = episode_id
    #     self.opening_crawl = opening_crawl
    #     self.director = director
    #     self.producers = producers
    #     self.release_date = release_date
    #     self.characters = characters
    #     self.planets = planets
    #     self.starships = starships
    #     self.vehicles = vehicles
    #     self.species = species
    #     self.url = url 

    @staticmethod
    def get(key):
        # TODO parse urls into references
        q = Films.construct_query(key)
        return requests.get(q).json()
        
    
    @staticmethod
    def get_dirty(url):
        return requests.get(url).json()
        
    @staticmethod
    def construct_query(key):
        if key == None:
            q = f"{config['api-url']}/films/"
            # raise Exception("Multiple resources not implemented yet")
        elif Utils.is_int_someway(key):
            # is_int_someway checks if is int or its str and a digit
            q = f"{config['api-url']}/films/{key}"
        else:
            # it's a string 
            pass   

        return q

        # utf-8 encoding
        # return urllib.parse.quote(q)
        
        