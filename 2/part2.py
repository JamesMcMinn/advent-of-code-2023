import re

sum = 0
with open("input.txt") as f:
    for line in f:
        power = 1
        for c in ["red", "green", "blue"]:
            power = power * max([int(x) for x in re.findall(r"([0-9]+) " + c, line)])
        sum += power
print(sum)
