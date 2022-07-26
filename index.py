'''Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. 
A dictionary consists of a collection of key-value pairs. 
Each key-value pair maps the key to its associated value.'''

class Dict:
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def getKeys(self):
        keys = [key for key, value in self.my_dict.items()]
        return keys

    def getValues(self):
        values = [value for key, value in self.my_dict.items()]
        return values
    

data = {'name': 'Simon', 'gender':'Male', 'residence':'Busia'}

my_dictionary = Dict(data)
print(my_dictionary.getValues())