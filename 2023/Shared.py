from functools import reduce


def sum(vals):
    return reduce(lambda x, y: x + y, vals)
