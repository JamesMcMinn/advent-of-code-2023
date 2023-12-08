seeds_str, *maps_str = open("input.txt").read().split("\n\n")

mappings = []
for m in maps_str:
    l: list[list[int]] = []
    for line in m[1:].split("\n", 1)[1].split("\n"):
        x = [int(x) for x in line.split()]
        l.append([x[0] - x[1], x[1], x[1] + x[2] - 1])
    mappings.append(l)

seeds = [int(x) for x in seeds_str.split(":")[1].split()]
sources: list[list[int]] = []
for i in range(0, len(seeds), 2):
    sources.append([seeds[i], seeds[i] + seeds[i + 1] - 1])

destinations: list[list[int]] = []
for section in mappings[:]:
    while sources:
        source, sources = sources[0], sources[1:]
        seed_min, seed_max = source
        for row in section:
            offset, row_min, row_max = row
            overlap = []
            # The seed contains the entire map row, so we split it into 3
            if seed_min < row_min and seed_max > row_max:
                overlap = [row_min, row_max]
                sources.append([seed_min, row_min - 1])
                sources.append([row_max + 1, seed_max])
            # The map row contains the "top" part of the seed, split into two
            elif seed_min < row_min and seed_max >= row_min:
                overlap = [row_min, seed_max]
                sources.append([seed_min, row_min - 1])
            # The map row contains all of the seed
            elif seed_min >= row_min and seed_max <= row_max:
                overlap = [seed_min, seed_max]
            # The map row contains the "bottom" part of the seed, split into two
            elif seed_min >= row_min and seed_min < row_max:
                overlap = [seed_min, row_max]
                sources.append([row_max + 1, seed_max])

            if overlap:
                destinations.append([overlap[0] + offset, overlap[1] + offset])
                break

        else:
            destinations.append(source)

    sources = destinations.copy()
    destinations = []
print(min([x[0] for x in sources]))
