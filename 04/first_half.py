from_to = [254032, 789860]
ans = 0
for number in range(from_to[0], from_to[1] + 1):
    digits = str(number)
    has_double = any([x * 2 in digits for x in '1234567890'])
    has_not_decrease = sorted(digits) == list(digits)
    if has_double and has_not_decrease:
        ans += 1

print(ans)
