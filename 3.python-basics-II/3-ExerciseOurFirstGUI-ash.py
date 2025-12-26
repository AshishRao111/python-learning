# Exercise!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

# replace 1 with * in gui
for i in picture:
    # x = 0
    for x in i:
        if x == 0:
            print(" ", end="")
        else:
            print("*", end="")
    # x += 1
    print("")
