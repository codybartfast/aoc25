class Device:
    def __init__(self, name, out_to):
        self.name = name
        self.out_to = out_to

        self.in_from = []
        self.path_count = None

    def __repr__(self):
        return f"Device({self.name}, {self.out_to}), path_count:{self.path_count}  in_from:   {self.in_from} "



def parse(input):
    devices = {name: Device(name, out_txt.split(" ")) for name, out_txt in [line.split(": ") for line in input.splitlines()]}
    devices["out"] = Device("out", [])
    for device in devices.values():
        if device.name == "you":
            device.path_count = 1
        for down_stream in device.out_to:
            devices[down_stream].in_from.append(device.name)
    return devices

def path_count(devices, device_name):
    device = devices[device_name]
    if device.path_count is not None:
        return device.path_count
    count = sum(path_count(devices, inner) for inner in device.in_from)
    device.path_count = count
    return count
    

def bells(input):
    devices = parse(input)

    yield None

    yield path_count(devices, "out")

    yield None


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    print("input: ", input)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(input_filename)
