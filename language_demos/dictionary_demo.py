

person = {
    "first_name": "Bob",
    "last_name": "Smith",
    "age": 23
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])

del person["last_name"]

# for key in person:
#     print(key)

# for (key, value) in person.items():
#     print(key, value)

# for key in person.keys():
#     print(key)

# for value in person.values():
#     print(value)

# print(person["last_name"])
# print(person.get("last_name"))
# print(person.get("last_name", "Smith"))

if "last_name" not in person:
    print("does not have last name")
else:
    print("has last name")


if 23 in person.values():
    print("person has a 23 value")
else:
    print("person does not have a 23 value")
