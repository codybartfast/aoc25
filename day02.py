import math
import re


def parse(input):
    return [
        (int(start), int(end))
        for [start, end] in [re.findall(r"\d+", span) for span in input.split(",")]
    ]


def does_repeat_size(size, n):
    f = 10**size
    pattern = n % f
    n //= f
    while n:
        if n % f != pattern:
            return False
        n //= f
    return True


def does_repeat(n):
    length = int(math.log10(n)) + 1
    for size in range(1, (length // 2) + 1):
        if length % size == 0:
            if does_repeat_size(size, n):
                return True


def is_double(n):
    length = int(math.log10(n)) + 1
    return length % 2 == 0 and does_repeat_size(length // 2, n)


def check_ids(id_range, is_invalid):
    start, end = id_range
    for n in range(start, end + 1):
        if is_invalid(n):
            yield n


def bells(input):
    id_ranges = parse(input)
    yield id_ranges
    yield sum([sum(check_ids(id_range, is_double)) for id_range in id_ranges])
    yield sum([sum(check_ids(id_range, does_repeat)) for id_range in id_ranges])


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    jingle()
