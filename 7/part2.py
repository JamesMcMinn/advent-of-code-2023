from collections import Counter

order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]
lines = open("input.txt").read().split("\n")
hands: list = [dict(zip(["cards", "bet"], x.split())) for x in lines]
hands = [h | {"counts": Counter(h["cards"])} for h in hands]
hands = [h | {"score": [order.index(x) for x in h["cards"][:]]} for h in hands]
for h in hands:
    jokers = h["counts"]["J"]
    h["counts"].subtract({"J": jokers})
    h["counts"].update({h["counts"].most_common()[0][0]: jokers})
hands.sort(key=lambda h: (sorted(list(h["counts"].values()), reverse=True), h["score"]))
print(sum([int(h["bet"]) * i for i, h in enumerate(hands, start=1)]))

# 249817836
