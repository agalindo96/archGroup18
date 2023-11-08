import os
import re


x = ''''''
list = []

'''
TODO: Validate filenames
'''
def validate(files):
    output = []
    for file in files:
        if not os.path.isfile("./data/" + file):
            print(f"File \'{file}\' does not exist!\n")
        else:
            output.append(file)

    return output



def get_addresses():
    with open('./data/Trace1.trc', 'r') as reader:
        file = reader.readlines()

        for i in range(0, 58, 3):
            read_size, address = re.search("\(0(.)\): ([0-9a-f]{8})", file[i]).groups()
            list.append("0x" + address + ": (" + read_size + ")\n")

    x = "".join(list)

    print(x)
