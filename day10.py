def parse(input):
    machines = []
    for line in input.splitlines():
        [pattern_txt, *butts_txt, jolt_txt] = line.split()
        pattern = 0
        bulb = 1
        for char in pattern_txt[1:-1]:
            if char == "#":
                pattern |= bulb
            bulb <<= 1
        buttons = []
        for butt_txt in butts_txt:
            button = 0
            for char in butt_txt[1:-1].split(","):
                button |= 1 << int(char)
            buttons.append(button)
        machines.append((pattern, buttons))
    return machines


def combinations(items):
    def unsorted_combos(items):
        if items:
            item = items[0:1]
            yield item
            for cmb in combinations(items[1:]):
                yield cmb
                yield item + cmb
        else:
            return []

    return sorted(unsorted_combos(items), key=lambda button: len(button))


def light_the_lights(pattern, combo):
    for combo in combinations(combo):
        lit = 0
        for button in combo:
            lit ^= button
            if lit == pattern:
                return len(combo)
        

def bells(input):
    machines = parse(input)
    yield None

    yield sum(light_the_lights(pattern, buttons) for [pattern, buttons, *_] in machines)
            
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
