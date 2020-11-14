import urllib.parse
import requests
from utils import Utils
from config import config
import json

import person, film

class swapi:

    @staticmethod
    def load(attribute, key):
        # TODO parse urls into references
        q = swapi.construct_query(attribute, key)
        return requests.get(q).json()
        
    @staticmethod
    def load_dirty(url):
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
        return film.Film(**film_dict)

        
    @staticmethod
    def get_people(key=None, url=None):
        if key != None: 
            people_dict = swapi.load('people', key)
        elif url != None:
            people_dict = swapi.load_dirty(url)
        else:
            return None

        if 'detail' in people_dict:
            return None

        if 'count' in people_dict:
            list_of_people_dict =  [person.Person(**i_dict) for i_dict in people_dict['results']] 

            while people_dict['next'] != None :
                if url != None:
                    people_dict = swapi.load_dirty(url=people_dict['next'])

                list_of_people_dict.extend([person.Person(**i_dict) for i_dict in people_dict['results']])

            return list_of_people_dict
        else:
            return person.Person(**people_dict)

        

        # deserialize a JSON string
    
    
if __name__ == "__main__":
    print("What star wars actually is: ")
    for i in range(1, 4):
        print("\t -> ", swapi.GetFilms(i))

    uno = swapi.GetFilms(1)
    for p in uno.characters:
        print(p)
        
        