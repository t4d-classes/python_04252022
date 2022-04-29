class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return self.first_name + " " + self.last_name

people = [
    Person('Bob', 'Smith'),
    Person('Sally', 'Jones'),
    Person('Abby', 'Timmons'),
    Person('Srilakshmi', 'Movva'),
    Person('Margrit', 'Zimmerman'),
    Person('Olivia', 'Rice'),
]

# people.sort(key=lambda p: p.first_name)

people_sorted = sorted(people, key=lambda p: p.first_name)

print(people)
print(people_sorted)