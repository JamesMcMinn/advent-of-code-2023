def first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char


if __name__ == "__main__":
    sum = 0
    with open("input.txt") as f:
        for line in f:
            first, last = first_digit(line), first_digit(line[::-1])
            sum += int(first + last)

    print(sum)
