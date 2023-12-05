total = 0
with open("input.txt") as f:
    for line in f:
        _, winning, have = line.replace(":", "|").split("|", 2)
        if (match := len(set(winning.split()) & set(have.split()))) > 0:
            total += 2 ** (match - 1)
print(int(total))
