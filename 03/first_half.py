with open("input.txt", "r") as f:
    data = [x.split(",") for x in f.read().split()]

decisions = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
points = (set(), set())

for i in range(2):
    x, y = 0, 0
    for ins in data[i]:
        for _ in range(int(ins[1:])):
            x += decisions[ins[0]][0]
            y += decisions[ins[0]][1]
            points[i].add((x, y))

same_points = points[0] & points[1]
print(min([abs(x) + abs(y) for (x, y) in same_points]))
