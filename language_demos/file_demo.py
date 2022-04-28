try:

    colors = []

    with open("colors.txt", "r") as colors_file:

        for color in colors_file:
            colors.append(color.rstrip())

    with open("colors2.txt", "w") as colors2_file:

        for color in colors:
            colors2_file.write(color + "\n")


except IOError as exc:
    print(exc)

finally:
    print("I always run whether there is an error or not...")