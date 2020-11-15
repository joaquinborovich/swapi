

import person

class Getter:

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


class Resource:

    def __init__(self, data_dictonary):
        for key, value in data_dictonary.items():
            setattr(self, f"_{key}", value)


class Film(Resource):

    def __init__(self, data_dictonary):
        super.__init__(data_dictonary)

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

class FilmGetter(Getter):

    @staticmethod
    def get(key):
        film_dict = super.load('films', key)
        if 'detail' in film_dict:
            # if film_dict['detail'] == 'Not found':
            return None

        # deserialize a JSON string
        return Film(film_dict)

class Person(Resource):

    def __init__(self, data_dictonary):
        super.__init__(data_dictonary)


    def __str__(self):
        return f"{self._name} ({self._url})"


class FilmGetter(Getter):

    @staticmethod
    def get(key=None, url=None):
        if key != None: 
            people_dict = super.load('people', key)
        elif url != None:
            people_dict = super.load_dirty(url)
        else:
            return None

        if 'detail' in people_dict:
            return None

        if 'count' in people_dict:
            list_of_people_dict =  [Person(i_dict) for i_dict in people_dict['results']] 

            while people_dict['next'] != None :
                if url != None:
                    people_dict = swapi.load_dirty(url=people_dict['next'])

                list_of_people_dict.extend([Person(i_dict) for i_dict in people_dict['results']])

            return list_of_people_dict
        else:
            return Person(people_dict)



