import itertools
import re

w = 141
f = ["."] * w + list(re.sub("[^0-9\*\.]", ".", open("input.txt").read())) + ["."] * w


def nums_around(i: int):
    l = list(itertools.takewhile(lambda x: x.isdigit(), reversed(f[i - w : i])))
    r = list(itertools.takewhile(lambda x: x.isdigit(), f[i + 1 : i + w]))
    m = f[i : i + 1]
    return [int(x) for x in "".join(l[::-1] + m + r).replace("*", ".").split(".") if x]


total = 0
for i in range(len(f)):
    if f[i] != "*":
        continue
    ratios = nums_around(i - w) + nums_around(i) + nums_around(i + w)
    total += ratios[0] * ratios[1] if len(ratios) == 2 else 0
print(total)
