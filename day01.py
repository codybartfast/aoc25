def parse(input_text):
    return [(line[0], int(line[1:])) for line in input_text.splitlines()]

def turn(start, instr):
    dir, turns = instr
    if turns % 100 == 0:
        raise NotImplementedError("This case probably not covered")
    stop = (start - turns if dir == 'L' else start + turns) % 100

    zero_clicks = turns // 100
    if (start != 0 and stop != 0 and
            ((dir == "L" and start < stop)
                or (dir == "R" and stop < start))):
        zero_clicks += 1
    return (stop, zero_clicks)
    
def bells(input_text):
    instructions = parse(input_text)
    yield instructions

    position = 50
    zero_stops = 0
    zero_clicks = 0
    for instr in instructions:
        position, clicks = turn(position, instr)
        zero_stops += position == 0
        zero_clicks += clicks

    yield zero_stops
    yield zero_stops + zero_clicks

def jingle(filename = None):
    import sack
    input_text = sack.read_input(filename)
    sack.present(lambda: bells(input_text))
    
               
if __name__ == "__main__":
    jingle()
