import re

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
f = open("input.txt").read()
for i, w in enumerate(words, 1):
    f = f.replace(w, w + str(i) + w)
print(sum([int(x[0] + x[-1]) for x in re.sub(r"[a-z]", "", f).splitlines()]))
