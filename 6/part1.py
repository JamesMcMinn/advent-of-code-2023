times_str, distances_str = open("input.txt").read().split("\n")
times = [int(x) for x in times_str.split(":")[1].split()]
distances = [int(x) for x in distances_str.split(":")[1].split()]
product = 1
for i, t in enumerate(times):
    product *= len([1 for x in range(t) if x * (t - x) > distances[i]])
print(product)
