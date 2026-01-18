from itertools import groupby


def parse(input):
    return [
        [int(x), int(y), int(z), idx]
        for idx, [x, y, z] in enumerate(
            [line.split(",") for line in input.splitlines()]
        )
    ]


def join_circuits(junctions, pair):
    ([_, _, _, c1], [_, _, _, c2]) = pair
    if c1 == c2:
        return False
    for j in junctions:
        if j[3] == c2:
            j[3] = c1
    return True


def signature(junctions):
    junctions.sort(key=lambda j: j[3])
    sizes = [len(list(group)) for _, group in groupby(junctions, key=lambda j: j[3])]
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def all_pairs(junctions):
    for idx1 in range(len(junctions) - 1):
        [x1, y1, z1, _] = (first := junctions[idx1])
        for idx2 in range(idx1 + 1, len(junctions)):
            [x2, y2, z2, _] = (second := junctions[idx2])
            dist_sqr = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            yield (dist_sqr, first, second)


def bells(input):
    junctions = parse(input)
    yield None

    trial = 1000

    pairs = list(all_pairs(junctions))
    pairs.sort(key=lambda pair: pair[0])

    trial_pairs = pairs[:trial]
    for _, j1, j2 in trial_pairs:
        join_circuits(junctions, (j1, j2))
    yield signature(junctions)

    last_pair = []
    for _, j1, j2 in pairs[trial:]:
        pair = (j1, j2)
        if join_circuits(junctions, pair):
            last_pair = pair
    yield last_pair[0][0] * last_pair[1][0]


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(input_filename)
