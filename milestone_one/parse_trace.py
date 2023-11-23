import os
import re

x = ''
list = []

def validate(files) -> list:
    output = []
    for file in files:
        if not os.path.isfile("./data/" + file):
            print(f"File \'{file}\' does not exist!\n")
        else:
            output.append(file)

    return output


# Modify to Return the addresses? Does another function depend on that output?
# TODO: Definitely need to modify
def get_addresses() -> None:
    with open('./data/Trace1.trc', 'r') as reader:
        file = reader.readlines()

        for i in range(0, 58, 3):
            read_size, address = re.search("\(0(.)\): ([0-9a-f]{8})", file[i]).groups()
            list.append("0x" + address + ": (" + read_size + ")\n")

    x = "".join(list)

    print(x)
