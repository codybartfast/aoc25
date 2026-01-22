def parse(input):
    [*shapes_txt, regions_txt] = input.split("\n\n")
    shapes = [
        [list(map(lambda c: 1 if c == '#' else 0, line)) for line in txt.splitlines()[1:]]
        for txt in shapes_txt]
        
    regions = []
    for region_txt in regions_txt.splitlines():
        left, right = region_txt.split(": ")
        size = tuple(map(int, left.split("x")))
        regions.append((size, list(map(int, right.split()))))
    return shapes, regions

def bells(input):
    shapes, regions = parse(input)
    sizes = [sum([sum(line) for line in shape]) for shape in shapes]
    available = [w * h for ((w, h), _) in regions]
    required = [sum(s * q for (s, q) in zip(sizes, region[1])) for region in regions]

    yield None
        
    yield sum(1 for (a, r) in zip(available, required) if a > r)

    yield "Merry Christmas"


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(input_filename)
