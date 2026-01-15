def parse(input_text):
    return [(line[0], int(line[1:])) for line in input_text.splitlines()]

def turn(start, instr):
    dir, turns = instr
    rslt = start - turns if dir == 'L' else start + turns
    return rslt % 100
    
def bells(input_text):
    instructions = parse(input_text)
    print(instructions, "\n")
    yield instructions

    position = 50
    values = [position]
    for instr in instructions:
        position = turn(position, instr)
        values.append(position)

    yield len([val for val in values if val == 0])
    yield None

def jingle(input_filename = None):
    import sack
    input_text = sack.read_input(input_filename)
    sack.present(lambda: bells(input_text))
    
    
if __name__ == "__main__":
    jingle()


