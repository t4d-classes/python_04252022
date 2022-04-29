name = "bob"

# simply does not work, easy to forget, but embrace
# the Python Experience!
# msg = "a" +
#     "b" +
#     "c"

# print(msg)

# nothing special needed here, but feels odd
msg = "".join([
    "a",
    name,
    "c"
])

print(msg)

# this allows for the creation of a multiline string,
# not a multiline string expression
# msg = """a
#    b
# c"""

# print(msg)

# the name expression can only be included
# if wrapped in an f-string
msg = "a" \
    f"{name}" \
    "c"

print(msg)

# the name expression can only be included
# if wrapped in an f-string
msg = (
    "a"
    f"{name}"
    "c"
)

print(msg)