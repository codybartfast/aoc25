def parse(input):
    return [[int(c) for c in line] for line in input.splitlines()]


# def best_two(bank):
#     idx, val1 = max(enumerate(bank[:-1]), key=lambda ivp: ivp[1])
#     val2 = max(bank[idx + 1:])
#     return val1 * 10 + val2


def best_n(n, bank):
    start = 0
    vals = []
    size = len(bank)
    while n > 0:
        idx, val = max(enumerate(bank[start : size - (n - 1)]), key=lambda ivp: ivp[1])
        vals.append(val)
        start += idx + 1
        n -= 1
    joltage = 0
    fact = 1
    while vals:
        joltage += fact * vals.pop()
        fact *= 10
    return joltage


def bells(input):
    batteries = parse(input)
    yield batteries

    yield sum([best_n(2, bank) for bank in batteries])

    yield sum([best_n(12, bank) for bank in batteries])


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(input_filename)
