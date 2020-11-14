# from resource_abstract_class import Resource
import urllib.parse

import utils

class Films():
    
    ATRIBUTE = 'films'

    def __init__(self, title, episode_id, opening_crawl, director, producers, release_date, characters, planets, starships, vehicles, species, url):
        self.title = title
        self.episode_id = episode_id
        self.opening_crawl = opening_crawl
        self.director = director
        self.producers = producers
        self.release_date = release_date
        self.characters = characters
        self.planets = planets
        self.starships = starships
        self.vehicles = vehicles
        self.species = species
        self.url = url 

    @staticmethod
    def get(key):
        q = Films.construct_query(key)

    @staticmethod
    def construct_query(key):
        if key == None:
            q = f"{self._api_url}/{ATRIBUTE}/"
            # raise Exception("Multiple resources not implemented yet")
        elif type(key) != int and key.is_digit():
            q = f"{self._api_url}/{ATRIBUTE}/{key}"
        else:
            # it's a string 
            pass   

            
        # utf-8 encoding
        return urllib.parse.quote(q)
        
        