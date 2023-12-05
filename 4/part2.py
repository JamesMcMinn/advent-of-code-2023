overlaps = []
for i, line in enumerate([line for line in open("input.txt")][::-1]):
    _, winning, have = line.replace(":", "|").split("|", 2)
    overlap = len(set(winning.split()) & set(have.split()))
    overlaps.append(1 + sum(overlaps[i - overlap : i]))
print(sum(overlaps))
