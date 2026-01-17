def parse(input):
    [part1, part2] = input.split("\n\n")
    id_ranges = [tuple(map(int, line.split("-"))) for line in part1.splitlines()]
    ids = list(map(int, part2.splitlines()))
    return id_ranges, ids


def is_in_naive(id, id_ranges):
    for start, end in id_ranges:
        if start <= id and id <= end:
            return True
    return False


def combine(range1, range2):
    (start1, end1), (start2, end2) = range1, range2
    if (
        (start1 <= start2 and start2 <= end1)
        or (start1 <= end2 and end2 <= end1)
        or (start2 <= start1 and start1 < end2)
    ):
        start = min(start1, start2)
        end = max(end1, end2)
        return (start, end)
    return None


def add(combined_ranges, new_range):
    for idx, old_range in enumerate(combined_ranges):
        if combined_range := combine(new_range, old_range):
            combined_ranges.pop(idx)
            add(combined_ranges, combined_range)
            return
    combined_ranges.append(new_range)


def bells(input):
    id_ranges, ids = parse(input)

    yield None

    yield len([id for id in ids if is_in_naive(id, id_ranges)])

    combined_ranges = []
    for new_range in id_ranges:
        add(combined_ranges, new_range)

    yield sum(1 + end - start for (start, end) in combined_ranges)


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"sack: filename: {input_filename}")
    jingle(input_filename)
