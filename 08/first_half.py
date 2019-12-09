import collections

with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().split()[0]]

width = 25
height = 6
min_zeros = -1
final = 0
for i in range(0, len(data), width * height):
    cur_zeros = dict(collections.Counter(data[i:i + width * height]))
    if cur_zeros[0] < min_zeros or min_zeros == -1:
        min_zeros = cur_zeros[0]
        final = cur_zeros[1] * cur_zeros[2]

print(final)
