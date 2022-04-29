class Person:

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def full_name(self):
    return self.first_name + " " + self.last_name


person1 = Person("Bob", "Smith")
print(person1.full_name())

person2 = Person("Jane", "Thomas")
print(person2.full_name())

