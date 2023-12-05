from dataclasses import dataclass

import Shared


@dataclass
class Range:
    source: int
    destination: int
    dist: int

    def contains(self, x):
        return x >= self.source and x < self.source+self.destination

    def map(self, x):
        diff = self.destination - self.source
        return x + diff


@dataclass
class RangeMap:
    name: str
    ranges: [Range]

    def map(self, x):
        for range in self.ranges:
            if range.contains(x):
                return range.map(x)
        return x


lines = open("./2023/Data/day5_sample.txt").readlines()


def seeds(line):
    line = line.replace("seeds: ", "")
    parts = line.split()
    return list(map(lambda x: int(x), parts))


def findNextMapLines(idx):
    while idx < len(lines) and len(lines[idx].strip()) > 0:
        yield lines[idx].strip()
        idx += 1


def mapLines():
    idx = 2
    while idx < len(lines):
        mapLines = list(findNextMapLines(idx))
        l = len(mapLines)
        # add 1 to skip empty lines
        idx += l + 1
        if l > 0:
            yield mapLines
        else:
            break


def rangeFromLine(line):
    parts = line.split()
    return Range(int(parts[1]), int(parts[0]), int(parts[2]))


def mapFromLines(lines):
    name = lines[0]
    ranges = list(map(rangeFromLine, lines[1:]))
    return RangeMap(name, ranges)


def allMaps():
    maps = mapLines()
    return list(map(mapFromLines, maps))


def parse(maps, val):
    for map in maps:
        val = map.map(val)
    return val


maps = allMaps()

test = [79, 14, 55, 13]
vals = map(lambda x: parse(maps, x), test)
print(list(vals))
