def parse(input):
    return input.splitlines()

def deflect(beams, row):
    nhits = 0
    new_beams = beams.copy()
    for idx, m in enumerate(row):
        nbeams = beams[idx]
        if nbeams > 0 and row[idx] == "^":
            nhits += 1
            new_beams[idx - 1] += nbeams
            new_beams[idx] = 0
            new_beams[idx + 1] += nbeams
             
    return new_beams, nhits

def part1(manifold):
    beams = [0] * len(manifold[0])
    beams[manifold[0].index("S")] = 1
    nhits = 0
    for row in manifold:
        beams, hits = deflect(beams, row)
        nhits += hits
    return nhits, sum(beams)
            
def bells(input):
    manifold = parse(input)

    yield None

    nhits, nbeams = part1(manifold)
    
    yield nhits

    yield nbeams


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"sack: filename: {input_filename}")
    jingle(input_filename)
