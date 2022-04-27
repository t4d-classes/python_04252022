# tuple
person1 = ('Bob', 'Smith')

#person1[2] = 44

print(person1[0])

person2 = {
  "first_name": "Bob",
  "last_name": "Smith"
}

person2["age"] = 44
 
print(person2["first_name"])


class Person:

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.age = 0


person3 = Person('Bob', 'Smith')

#person3.age = 44

print(person3.first_name)
print(person3.age)
