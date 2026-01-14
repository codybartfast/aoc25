def parse(input_text):
    return input_text

def part1(input):
    ...

def part2(input):
    ...

def bells(input_text):
    input = parse(input_text)
    print(input)
    ans1 = part1(input)
    ans2 = part2(input)
    print(f"Part1: {ans1}")
    print(f"Part2: {ans2}")

def jingle(input_filename = None):
    import sack
    input_text = sack.get_input(input_filename)
    bells(input_text)

if __name__ == "__main__":
    jingle("test1")
