

class Film:

    def __init__(self, title, episode_id, opening_crawl, director, producer, release_date, characters, planets, starships, vehicles, species, url, created, edited):
        self.title = title
        self.episode_id = episode_id
        self.opening_crawl = opening_crawl
        self.director = director
        self.producer = producer
        self.release_date = release_date
        self.characters = characters
        self.planets = planets
        self.starships = starships
        self.vehicles = vehicles
        self.species = species
        self.url = url

    def __str__(self):
        return f"{self.title} ({self.url})"