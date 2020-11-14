

# from swapi import swapi


class Person:

    def __init__(self, name, birth_year, eye_color,  gender, hair_color, height, mass, skin_color, homeworld, films, species, starships, vehicles, url, created, edited):
        self._name = name
        self._birth_year = birth_year
        self._eye_color = eye_color
        self._gender = gender
        self._hair_color = hair_color
        self._height = height
        self._mass = mass
        self._skin_color = skin_color
        self._homeworld = homeworld
        self._films = films
        self._species = species
        self._starships = starships
        self._vehicles = vehicles
        self._url = url
        self._created = created
        self._edited = edited

    def __str__(self):
        return f"{self._name} ({self._url})"
