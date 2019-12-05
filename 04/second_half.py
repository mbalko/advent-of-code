from_to = [254032, 789860]
ans = 0
for number in range(from_to[0], from_to[1] + 1):
    digits = str(number)
    has_not_decrease = sorted(digits) == list(digits)
    has_lower_double = any([x * 2 in digits and not x * 3 in digits for x in '1234567890'])
    if has_not_decrease and has_lower_double:
        ans += 1

print(ans)
