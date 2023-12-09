from collections import Counter

points = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][::-1]
hands = sorted(
    [x.split() for x in open("input.txt").read().split("\n")],
    key=lambda h: (
        sorted([x for x in Counter(h[0]).values()], reverse=True),
        [points.index(x) for x in h[0][:]],
    ),
)
print(sum([int(h[1]) * i for i, h in enumerate(hands, start=1)]))
