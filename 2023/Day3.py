import Shared

lines = open("./2023/Data/day3.txt").readlines()

lines = list(map(lambda l: f".{l.strip()}.", lines))


def isSymbol(x, y):
    if x < 0 or y < 0:
        return False
    if y >= len(lines) or x >= len(lines[y]):
        return False
    symbol = lines[y][x]
    if symbol.isdigit() or symbol == ".":
        return False
    return True


def adjacent(x, y):
    yield x+1, y-1
    yield x+1, y
    yield x+1, y+1
    yield x-1, y-1
    yield x-1, y
    yield x-1, y+1
    yield x, y-1
    yield x, y+1


def isPartNumber(x, y):
    for aX, aY in adjacent(x, y):
        if isSymbol(aX, aY):
            return True

    return False


def numbersFromLine(y):
    line = lines[y]
    x = 0
    w = -1
    c = ""
    while x < len(line):
        if line[x].isdigit():
            if w == -1:
                w = x
            c += line[x]
        elif w >= 0:
            yield w, c
            w = -1
            c = ""
        x += 1
    if w >= 0:
        yield w, c


def partNumbersFromLine(y):
    numbers = numbersFromLine(y)
    for pos, num in numbers:
        for x in range(len(num)):
            if isPartNumber(pos+x, y):
                yield num
                break


def partNumbersFromLines():
    for y in range(len(lines)):
        numbers = partNumbersFromLine(y)
        for number in numbers:
            yield int(number)


vals = partNumbersFromLines()
val = sum(vals)
print(f"Result 1: {val}")

# print(list(partNumbersFromLine(4)))
partNumbersMap = {}

for y in range(len(lines)):
    numbers = numbersFromLine(y)
    for pos, num in numbers:
        for x in range(len(num)):
            partNumbersMap[pos + x, y] = int(num)


def partNumberAt(x, y):
    for aX, aY in adjacent(x, y):
        if (aX, aY) in partNumbersMap:
            yield partNumbersMap[aX, aY]


def gearRatios():
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if line[x] == "*":
                partNumbers = list(set(partNumberAt(x, y)))
                if len(partNumbers) == 2:
                    yield partNumbers[0] * partNumbers[1]


ratios = list(gearRatios())
val = sum(ratios)

print(f"Result 2: {val}")
