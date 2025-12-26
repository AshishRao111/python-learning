# Exercise:Find duplicates
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []

for item in some_list:
    count = 0
    for x in some_list:
        if item == x:
            count += 1
    if count > 1 and item not in duplicates:
        duplicates.append(item)

print(duplicates)
