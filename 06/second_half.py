with open("input.txt", "r") as f:
    data = {x.split(")")[1]:x.split(")")[0] for x in f.read().split()}

sum = 0
you_parents = []
san_parents = []

parent = data["YOU"]
while parent in data:
    you_parents.append(parent)
    parent = data[parent]

parent = data["SAN"]
while parent in data:
    san_parents.append(parent)
    parent = data[parent]
    if parent in you_parents:
        sum = len(san_parents) + you_parents.index(parent)
        break

print(sum)
