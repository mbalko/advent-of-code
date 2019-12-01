fuel = 0

with open("input.txt", "r") as f:
    data = f.read().split()

for number in data:
    fuel += int(int(number) / 3) - 2 # double casting to get floor

print(fuel)
