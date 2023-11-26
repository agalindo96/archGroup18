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
# TODO: Definitely need to modify to get all the trace data for the simulation
def parse_trace(file) -> None:
    with open('./data/Trace1.trc', 'r') as reader:
        lines = reader.readlines()
        for line in lines: 
            result = re.search("\(0(.)\): ([0-9a-f]{8})", line)

            if result:
                read_length, instruction_address = result.group(1), result.group(2)
            

            # #matches = re.finditer("M: (^00;(?!0+$)\d{8}$)", line)
            #print(read_length, instruction_address)
            
            # for match in matches:
            #     print(match.group(1))
            #list.append("0x" + address + ": (" + read_size + ")\n")
            
