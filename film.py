from swapi import swapi

import person

class Film:

    def __init__(self, title, episode_id, opening_crawl, director, producer, release_date, characters, planets, starships, vehicles, species, url, created, edited):
        self._title = title
        self._episode_id = episode_id
        self._opening_crawl = opening_crawl
        self._director = director
        self._producer = producer
        self._release_date = release_date
        self._characters = characters
        self._planets = planets
        self._starships = starships
        self._vehicles = vehicles
        self._species = species
        self._url = url

    def __str__(self):
        return f"{self._title} ({self._url})"

    @property
    def title():
        return self._title
    
    @property
    def characters(self):
        chars = []
        for character in self._characters:
            chars.append(swapi.get_people(url=character))
        
        return chars



