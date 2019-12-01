def calculate_fuel(current, total = 0):
    new = int(current / 3) - 2
    if new < 0:
        return total
    return calculate_fuel( new, total + new )

fuel = 0

with open("input.txt", "r") as f:
    data = f.read().split()

for number in data:
    fuel += calculate_fuel(int(number))

print(fuel)
