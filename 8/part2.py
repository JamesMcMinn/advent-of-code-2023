import re
import math

pattern, _, *nodes = re.sub("[=\(,\)]", "", open("input.txt").read()).split("\n")
mapping = {y[0]: {"L": y[1], "R": y[2]} for y in [x.split() for x in nodes]}
starting_nodes = [k for k in mapping if k[-1] == "A"]
steps: list[int] = [0] * len(starting_nodes)
for i, location in enumerate(starting_nodes):
    while location[-1] != "Z":
        location = mapping[location][pattern[steps[i] % len(pattern)]]
        steps[i] += 1
print(math.lcm(*steps))
