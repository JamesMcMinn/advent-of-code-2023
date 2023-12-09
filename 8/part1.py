import re

pattern, _, *nodes = re.sub("[=\(,\)]", "", open("input.txt").read()).split("\n")
mapping = {y[0]: {"L": y[1], "R": y[2]} for y in [x.split() for x in nodes]}
location, step = "AAA", 0
while location != "ZZZ":
    location = mapping[location][pattern[step % len(pattern)]]
    step += 1
print(step)
