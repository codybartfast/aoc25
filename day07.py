def parse(input):
    return input.splitlines()

def deflect(beams, row):
    hits = [idx for idx, m in enumerate(row) if beams[idx] == 1 and row[idx] == "^"]    
    for hit in hits:
        # if hit > 0:
        beams[hit - 1] = 1
        beams[hit] = 0
        # if hit < len(beams) - 1:
        beams[hit + 1] = 1
    return len(hits)

def part1(manifold):
    beams = [0] * len(manifold[0])
    beams[manifold[0].index("S")] = 1
    nhits = 0
    for row in manifold:
        nhits += deflect(beams, row)
    return nhits
            
def bells(input):
    manifold = parse(input)
    # print(manifold, "\n")

    yield None

    yield part1(manifold)

    yield None


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"sack: filename: {input_filename}")
    jingle(input_filename)
