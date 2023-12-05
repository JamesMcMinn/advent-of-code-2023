import re

w = 141
f = ["."] * w + list(open("input.txt").read().replace("\n", ".")) + ["."] * w
s = 0
total = 0
for i in range(len(f)):
    s = i if f[i].isdigit() and not s else s
    if s and not f[i].isdigit():
        b = f[s - w - 1 : i - w + 1] + f[s - 1 : i + 1] + f[s + w - 1 : i + w + 1]
        if re.sub(r"[0-9.]", "", "".join(b)):
            total += int("".join(f[s:i]))
        s = 0
print(total)
