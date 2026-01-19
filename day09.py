# import math


def parse(input):
    return [tuple(map(int, line.split(","))) for line in input.splitlines()]


def find_rectangles(reds):
    for i in range(len(reds) - 1):
        for j in range(i + 1, len(reds)):
            yield reds[i], reds[j]


def rect_size(corners):
    ((x1, y1), (x2, y2)) = corners
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def to_lines(reds):
    reds.append(reds[0])
    return list(zip(reds, reds[1:]))


def is_between(x, a, b):
    if a > b:
        a, b = b, a
    return a < x and x < b


def is_horizontal(line):
    (x1, y1), (x2, y2) = line
    return x1 != x2


def contains(rectangle, tile):
    (x1, y1), (x2, y2) = rectangle
    (x, y) = tile
    return is_between(x, x1, x2) and is_between(y, y1, y2)


def contains_red(rectangle, reds):
    return any(contains(rectangle, red) for red in reds)


def find_intersection(line_a, line_b):
    (((ax1, ay1), (ax2, ay2)), ((bx1, by1), (bx2, by2))) = line_a, line_b
    if ax1 != ax2:
        assert bx1 == bx2
        return find_intersection(line_b, line_a)
    if is_between(ax1, bx1, bx2) and is_between(by1, ay1, ay2):
        return (ax1, by1)
    else:
        return None


def is_crossed(rectangle, horizontal_lines):
    (x1, y1), (x2, y2) = rectangle
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    left = (min_x, min_y + 1), (min_x, max_y - 1)
    right = (max_x, min_y + 1), (max_x, max_y - 1)

    for line in horizontal_lines:
        if find_intersection(left, line) or find_intersection(right, line):
            return True
    return False


def find_green(reds, rectangles):
    lines = to_lines(reds)
    horizontal_lines = [line for line in lines if is_horizontal(line)]

    biggest = 0
    for rect in rectangles:
        size = rect_size(rect)
        if size > biggest:
            if not contains_red(rect, reds):
                if not is_crossed(rect, horizontal_lines):
                    biggest = size
    return biggest


def bells(input):
    reds = parse(input)
    yield None

    rectangles = list(find_rectangles(reds))
    yield max(map(rect_size, rectangles))
    yield find_green(reds, rectangles)


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"sack: filename: {input_filename}")
    jingle(input_filename)
