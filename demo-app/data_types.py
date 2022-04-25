# Explore Data Types

some_var = None
print(type(some_var))

some_var = 2
print(type(some_var))

some_var = 5.6
print(type(some_var))

some_var = False # True
print(type(some_var))

some_var = (1, "fun", True)
print(type(some_var))

some_var = [1,2,3,4,5]
print(type(some_var))

def do_it():
    print("did it")

do_it()
some_var = do_it
print(type(some_var))


some_var = int("23")
print(some_var)
print(type(some_var))

some_var = bool(None)
print(some_var)
print(type(some_var))

