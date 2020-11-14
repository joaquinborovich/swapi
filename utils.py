class Utils:

    @staticmethod
    def is_int_someway(key):
        if type(key) == int:
            return True
        if type(key) == str and key.is_digit():
            return True
        
        else return False