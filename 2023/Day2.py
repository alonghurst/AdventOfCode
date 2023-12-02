from dataclasses import dataclass
from functools import reduce


@dataclass
class Game:
    id: int
    results: [{}]

lines = open("./2023/Data/day2.txt").readlines()

def parseLineToGame(line):
    line = line.replace("Game ", "")
    parts = line.split(":")

    id = int(parts[0])
    results = []
    
    parts = parts[1].split(";")
    for part in parts:
        dict = {}
        subparts = part.split(", ")
        for subpart in subparts:
            entry = subpart.split()
            v = int(entry[0])
            k = entry[1].strip()
            dict[k] = v
        results.append(dict)
    
    return Game(id, results)

def isPossible(terms, game):
    for result in game.results:
        for gKey,gValue in result.items():
            for tKey,tValue in terms.items():
                if tKey == gKey and gValue > tValue:
                    return False
    return True

def isPossibleCurry(terms):
    def curry(game):
        return isPossible(terms, game)
    return curry

def minimumCubes(game):
    dict = {}
    for result in game.results:
        for key,value in result.items():
            if key in dict:
                if dict[key] < value:
                    dict[key] = value
            else:
                dict[key] = value
    return dict

def powerOf(dict):
    val = 1
    for key,value in dict.items():
        val *= value
    return val

sampleTerms = {
    "red": 12,
    "green": 13,
    "blue": 14
}

games = list(map(parseLineToGame, lines))
impossibleGames = list(filter(isPossibleCurry(sampleTerms), games))
vals = map(lambda x: x.id, impossibleGames)
result = reduce(lambda x, y: x + y, vals)

print(f"Result 1: {result}")

minCubes = map(minimumCubes, games)
vals = map(powerOf, minCubes)
result = reduce(lambda x, y: x + y, vals)

print(f"Result 2: {result}")