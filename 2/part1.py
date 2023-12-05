import re

sum = 0
with open("input.txt") as f:
    for line in f:
        for k, v in {"red": 12, "green": 13, "blue": 14}.items():
            if max([int(x) for x in re.findall(r"([0-9]+) " + k, line)]) > v:
                break
        else:
            sum += int(re.match("Game ([0-9]+)", line).group(1))
print(sum)
