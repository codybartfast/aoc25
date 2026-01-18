def split(beams, row):
    nhits = 0
    new_beams = beams.copy()
    for idx, (item, nbeams) in enumerate(zip(row, beams)):
        nbeams = beams[idx]
        if nbeams > 0 and item == "^":
            nhits += 1
            new_beams[idx - 1] += nbeams
            new_beams[idx] = 0
            new_beams[idx + 1] += nbeams

    return new_beams, nhits


def shine(manifold):
    beams = [0] * len(manifold[0])
    beams[manifold[0].index("S")] = 1
    nhits = 0
    for row in manifold:
        beams, hits = split(beams, row)
        nhits += hits
    return nhits, sum(beams)


def bells(input):
    manifold = input.splitlines()
    yield None
    yield from shine(manifold)


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"sack: filename: {input_filename}")
    jingle(input_filename)
