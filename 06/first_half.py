with open("input.txt", "r") as f:
    data = {x.split(")")[1]:x.split(")")[0] for x in f.read().split()}

sum = 0
for i in data:
    sum += 1
    parent = data[i]
    while parent in data:
        sum += 1
        parent = data[parent]

print(sum)
