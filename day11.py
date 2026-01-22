class Device:
    def __init__(self, name, out_to):
        self.name = name
        self.out_to = out_to


def parse(input):
    devices = {
        name: Device(name, out_txt.split(" "))
        for name, out_txt in [line.split(": ") for line in input.splitlines()]
    }
    devices["out"] = Device("out", [])
    for device in devices.values():
        device.out_to = [devices[name] for name in device.out_to]
    return devices


def path_count(devices, start, end):
    start, end = devices[start], devices[end]
    counts = {end: 1}

    def search(start):
        if start in counts:
            return counts[start]
        count = sum(search(outer) for outer in start.out_to)
        counts[start] = count
        return count

    return search(start)


def bells(input):
    devices = parse(input)

    yield devices

    yield path_count(devices, "you", "out")

    yield (
        path_count(devices, "svr", "dac")
        * path_count(devices, "dac", "fft")
        * path_count(devices, "fft", "out")
    ) + (
        path_count(devices, "svr", "fft")
        * path_count(devices, "fft", "dac")
        * path_count(devices, "dac", "out")
    )


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(input_filename)
