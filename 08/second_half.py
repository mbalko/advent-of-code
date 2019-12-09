with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().split()[0]]

width = 25
height = 6
size = width * height

layers = []
final_image = ""
for i in range(0, len(data), size):
    layers.append(data[i:i + size])

for pixel in range(size):
    if not pixel % width:
        final_image += "\n"
    i = 0
    while layers[i][pixel] == 2:
        i += 1
    final_image += " " if not layers[i][pixel] else "#"

print(final_image)
