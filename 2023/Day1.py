from functools import reduce

f = open("./2023/Data/day1_sample.txt")

lines = f.readlines()

replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def numFromLine(line):
    digits = [i for i in line if i.isdigit()]

    print(f"{line} -> {digits}")

    a = digits[0]
    b = digits[-1]
    return int(a + b)

def fixLines(line):
    indexes = [(key, value, line.find(key), line.rfind(key)) for key, value in replacements.items()]

    return line

vals = map(numFromLine, lines)
result = reduce(lambda x, y: x + y, vals)

print(f"Part 1: {result}")

