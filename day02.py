import re


def parse(input):
    return [
        (int(start), int(end))
        for [start, end] in [re.findall("\d+", span) for span in input.split(",")]
    ]

def is_double(n):
    ntxt = str(n)
    lng = len(ntxt)
    return lng % 2 == 0 and ntxt[0:lng//2] == ntxt[lng//2:]

def check_ids(id_range, is_invalid):
    start, end = id_range
    for n in range(start, end + 1):
        if is_invalid(n):
            yield n

def bells(input):
    data = parse(input)
    print(data, "\n")
    yield data
    # for id_range in data:
    #     print(sum(check_ids(id_range, is_double)))
    yield sum([sum(check_ids(id_range, is_double)) for id_range in data])
    yield None


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    # jingle("test1")
    jingle()
