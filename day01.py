
def bells(input):
    print("Hello from aoc25!")
    print(input)
    print("Goodbye form aoc25")

def jingle(input_filename = None):
    import sack
    input = sack.get_input(input_filename)
    print(input)
    bells(input)

if __name__ == "__main__":
    jingle()
