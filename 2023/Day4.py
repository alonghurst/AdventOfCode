import Shared

lines = open("./2023/Data/day4.txt").readlines()


def strToNum(str):
    split = str.split()
    return list(map(lambda x: int(x), split))


def readCard(line):
    split = line.split(":")[1].split("|")
    winning = strToNum(split[0])
    haves = strToNum(split[1])
    return winning, haves


def winnersFromLine(line):
    winning, haves = readCard(line)
    winners = list(filter(lambda x: x in winning, haves))
    return winners


def points(winners):
    if len(winners) == 0:
        return 0
    val = 1
    x = 1
    while x < len(winners):
        x += 1
        val *= 2
    return val


def pointsFromLine(line):
    winners = winnersFromLine(line)
    return points(winners)


def additionalCardsForLine(line, index):
    winners = winnersFromLine(line)
    x = 0
    while x < len(winners):
        x += 1
        yield index + x


def processCopyingCards(lines):
    processed = 0
    toProcess = [x for x in range(len(lines))]
    while len(toProcess) > 0:
        processing = toProcess.pop()
        if processing >= len(lines):
            continue
        processed += 1
        additional = additionalCardsForLine(lines[processing], processing)
        toProcess.extend(additional)
    return processed


vals = map(pointsFromLine, lines)
result = sum(vals)
print(f"Result 1: {result}")

print(len(lines))

print(list(additionalCardsForLine(lines[206], 207)))

result = processCopyingCards(lines)
print(f"Result 2: {result}")
