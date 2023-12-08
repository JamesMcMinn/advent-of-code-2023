seeds, *maps = open("input.txt").read().split("\n\n")
mappings = []
for m in maps:
    mappings.append(
        [list(map(int, line.split())) for line in m[1:].split("\n", 1)[1].split("\n")]
    )

locations = []
for seed in map(int, seeds.split(":")[1].split()):
    route = seed
    for section in mappings:
        for d in section:
            if (route >= d[1]) and (route < (d[1] + d[2])):
                route = d[0] + (route - d[1])
                break
    locations.append(route)
print(min(locations))
