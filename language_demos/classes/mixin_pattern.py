# import json
import jsonpickle
import yaml

class ItemListJsonMixin:

    # def to_json(self):
    #     return json.dumps(self._items)

    def to_json(self):
        return jsonpickle.encode(self._items)


class ItemListYamlMixin:

    def to_yaml(self):
        return yaml.dump(self._items)   

class ItemList:

    def __init__(self):
        self._items = []


class PeopleList(ItemList, ItemListJsonMixin, ItemListYamlMixin):

    def __init__(self):
        super().__init__()


    def __add__(self, person):
        # __dict__ used for the built-in JSON module
        # self._items.append(person.__dict__)

        # jsonpickle package can serialize custom objects
        self._items.append(person)
        return self


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + " " + self.last_name




people = PeopleList()

people += Person('Bob', 'Smith')
people += Person('Sally', 'Jones')

print(people.to_json())
print(people.to_yaml())