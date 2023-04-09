def largest_sum(s):
    total = 0
    temp_total = 0
    for i in range(0, len(s)):
        if s[i] != "0":
            temp_total += int(s[i])
        else:
            total = max(temp_total, total)
            temp_total = 0
    return total

print(largest_sum("72102450111111090"))
