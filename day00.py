def parse(input_text):
    return input_text

def bells(input_text):
    input = parse(input_text)
    print(input, "\n")
    yield input
    yield None
    yield None

def jingle(input_filename = None):
    import sack
    input_text = sack.read_input(input_filename)
    sack.present(lambda: bells(input_text))
    
    
if __name__ == "__main__":
    jingle("test1")
