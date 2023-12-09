data = open("input.txt").read().replace(" ", "").split("\n")
time, distance = int(data[0].split(":")[1]), int(data[1].split(":")[1])
print(len([True for x in range(time) if x * (time - x) > distance]))
