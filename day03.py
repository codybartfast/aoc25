def parse(input):
    return [[int(c) for c in line] for line in input.splitlines()]

def best_two(bank):
    idx, val1 = max(enumerate(bank[:-1]), key=lambda ivp: ivp[1])
    val2 = max(bank[idx + 1:])
    return val1 * 10 + val2

def bells(input):
    battery = parse(input)
    print(battery, "\n")
    yield battery

    yield sum([best_two(bank) for bank in battery])

    yield None


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(input_filename)
