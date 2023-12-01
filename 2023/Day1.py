from functools import reduce

f = open("./2023/Data/day1.txt")

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

    #print(f"{line} -> {digits}")

    a = digits[0]
    b = digits[-1]
    return int(a + b)

def fixLine(line):
    indexes = [(key, value, line.find(key), line.rfind(key)) for key, value in replacements.items()]

    forwards = (
        (idx[0], idx[1], idx[2]) for idx in sorted(indexes, key=lambda x: x[2])
        if idx[2] >= 0
    )
    backwards = (
        (idx[0], idx[1], idx[3]) for idx in sorted(indexes, key=lambda x: -x[3])
        if idx[3] >= 0
    )

    a = next(forwards, ("", "", -1))
    b = next(backwards, ("", "", -1))

    fixedLine = line

    if a[2] >= 0:
        fixedLine = fixedLine[:a[2]] + a[1] + fixedLine[a[2] + 1:]
    if b[2] >= 0:
        fixedLine = fixedLine[:b[2]] + b[1] + fixedLine[b[2] + 1:]
    
    # print(f"{line} -> {fixedLine} -> {numFromLine(fixedLine)}")
    # print(indexes)

    return fixedLine

vals = map(numFromLine, lines)
result = reduce(lambda x, y: x + y, vals)

print(f"Part 1: {result}")

lines = map(fixLine, lines)
vals = map(numFromLine, lines)
result = reduce(lambda x, y: x + y, vals)

print(f"Part 2: {result}")

lines = open("./2023/Data/day1_compare.txt").readlines()

def compare(line):
    parts = line.split(",")
    fixed = fixLine(parts[0])
    val = numFromLine(fixed)
    val2 = int(parts[1])
    if(val != val2):
        print (f"{line} ({val})")
    return 1

for line in lines:
    compare(line)