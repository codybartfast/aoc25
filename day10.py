import math


def parse(input):
    machines = []
    for line in input.splitlines():
        [pattern_txt, *butts_txt, jolts_txt] = line.split()
        pattern = 0
        bulb = 1
        for char in pattern_txt[1:-1]:
            if char == "#":
                pattern |= bulb
            bulb <<= 1
        light_masks = []
        jolts = [int(n) for n in jolts_txt[1:-1].split(",")]
        buttons = []
        for butt_txt in butts_txt:
            mask = 0
            button = [0] * len(jolts)
            for n in [int(char) for char in butt_txt[1:-1].split(",")]:
                mask |= 1 << n
                button[n] = 1
            light_masks.append(mask)
            buttons.append(tuple(button))
        machines.append((pattern, light_masks, buttons, jolts))
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


def light_the_lights(pattern, light_masks):
    for combo in combinations(light_masks):
        lit = 0
        for button in combo:
            lit ^= button
            if lit == pattern:
                return len(combo)


def press_the_buttons(buttons, jolts, target, other_buttons, count):
    [button, *rest] = buttons
    if not rest:
        remaining = jolts[target]
        jolts_after = list(map(lambda b, j: j - b * remaining, button, jolts))
        if any(j for j in jolts_after if j < 0):
            return None
        return jolt_the_jolts(other_buttons, jolts_after, count + remaining)

    max_press = min([j for (b, j) in zip(button, jolts) if b > 0])

    best_count = math.inf
    for press_count in range(max_press, -1, -1):
        jolts_after = [j - (b * press_count) for (b, j) in zip(button, jolts)]
        solution = press_the_buttons(
            rest,
            jolts_after,
            target,
            other_buttons,
            count + press_count,
        )
        if solution is not None:
            if solution < best_count:
                best_count = solution
    if best_count == math.inf:
        return None
    return best_count


def jolt_the_jolts(buttons, jolts, count):
    if all(j == 0 for j in jolts):
        return count

    if not buttons:
        return None
    cover = list(map(lambda *vals: sum(vals), *buttons))
    if not all(c >= 1 or j == 0 for (c, j) in zip(cover, jolts)):
        return None

    target = min(
        [ivp for ivp in enumerate(cover) if ivp[1] > 0], key=lambda ivp: ivp[1]
    )[0]

    target_butts = sorted([button for button in buttons if button[target]])
    buttons = [butt for butt in buttons if butt not in target_butts]

    rslt = press_the_buttons(target_butts, jolts, target, buttons, count)
    return rslt


def bells(input):
    machines = parse(input)
    # print(input)
    yield None

    yield sum(
        light_the_lights(pattern, light_masks)
        for [pattern, light_masks, *_] in machines
    )

    print("\nGo pick a good movie and then check how I'm doing ...\n")
    yield sum(jolt_the_jolts(buttons, jolts, 0) for _, _, buttons, jolts in machines)


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"sack: filename: {input_filename}")
    jingle(input_filename)
