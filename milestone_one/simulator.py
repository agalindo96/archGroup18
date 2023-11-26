import math
import re

import constants
from cache import Cache


# TODO: Delete parse_trace.py
# Helper function that finds all valid addresses in a given line, returns a dict of addresses and each of their lengths
def get_memory_accesses(line) -> dict:
    memory_accesses = {}
    eip_search = re.search("\(0(.)\): ([0-9a-f]{8})", line)

    # If the previous search pattern was found in the line
    if eip_search:
        # eip_search.group(2): the address of the instruction (int)
        # Python treats hex digits as ints, which is why we're storing it as one
        # eip_search.group(1): the length of that instruction (int)
        memory_accesses[eip_search.group(2)] = int(eip_search.group(1))
    # The line didn't match the previous search pattern, so 'line' must be the data line
    else:
        # First search pattern group (?!0{8}) exludes instances where addresses are all zeros (00000000)
        # Search pattern will match the following cases:
        #   dstM has a valid address, srcM has a valid address, BOTH dstM and srcM have valid addresses
        data_search = re.findall(": (?!0{8})([0-9a-f]{8})", line)
        # If we found at least one valid address
        if data_search:
            for address in data_search:
                # Add each valid address in the data_search list to the dict, use the given constant for the length
                memory_accesses.update({address: constants.DATA_ACCESS_LENGTH})
    # If there are no valid addresses in this line, return None
    # Would only happen on the data line where both dstM and srcM are set to 00000000
    if not memory_accesses:
        return None

    return memory_accesses


# Gets a string representing a memory address and two integers representing the number of bytes in the tag and index
# Returns a tuple containing the values for tag, index, and offset by slicing the address string along the bounds
def split_address(address, tag_size, index_size) -> tuple:
    # Converts the hex address string to a binary string
    # We add "1" and slice from index 3 to preserve addresses with an MSB = 0
    # Ex.
    #       bin(int("0A38", 16)) -> '0b101000111000'        MSB is NOT preserved (int() collapses leading zeros)
    #   bin(int("1"+"0A38", 16)) -> '0b10000101000111000'
    #  '0b10000101000111000'[3:] -> '0000101000111000       All trailing zeros are preserved
    binary_address = bin(int("1" + address, base=16))[3:]

    # The bit where the index starts from (left to right)
    index_shift = tag_size
    # The bit where the offset starts from
    offset_shift = index_shift + index_size

    # Hex conversion in Python is tricky, we use padding to ensure any leading zero is preserved
    # tag_size / 4 is how many hex digits are in the tag, Math.ceil() rounds up in case tag size % 4 != 0
    # 4 is the number of bits in a single hex digit, +2 because of the prepended '0x'
    padding = math.ceil(tag_size / 4) + 2

    tag = f"{int(binary_address[:index_shift], base=2):#0{padding}x}"
    index = hex(int(binary_address[index_shift:offset_shift], base=2))
    offset = hex(int(binary_address[offset_shift:], base=2))

    return (
        tag,
        index,
        offset,
    )


# TODO: What are we supposed to do for the last memory access where instruction length is zero?
# Simulator.py will replace parse_trace.py.
# Here's what it does as of now:
#   - Fully parses the trace files, gets valid addresses and lengths per line
#   - Can extract tag, index, and offset data from an address
# TODO: We still need to actually DO something with this information
#       read/write methods? Would there even be a difference in this case?
#       How do we represent data being in a byte in a cache block?
#           Set bytes = 1?
#       Eventually want to return a dict called "results" containing all the info for the next print function
#           - Total Cache Accesses               - Hit Rate
#           - Cache Hits                         - Miss Rate
#           - Cache Misses                       - CPI
#           - Compulsory Misses                  - Unused Cache Space
#           - Conflict Misses                    - Waste
#                                                - Unused Cache Blocks
# # Files accessed (counter) is the same as his for small trace files, but slightly different for larger trace files
def simulate(cache, data, file) -> dict:
    counter = 0

    with open(f"./data/{file}", "r") as reader:
        lines = reader.readlines()

        for line in lines:
            # If the current line is not blank
            if line:
                memory_accesses = get_memory_accesses(line)

            # If there is at least one valid memory access in this line
            if memory_accesses:
                for address, length in memory_accesses.items():
                    tag, index, offset = split_address(
                        address, data["tag_size"], data["index_size"]
                    )
                    counter += 1
                    # print(tag, index, offset)
                    # f = split_address(address, data)

                    # for i in range(len(f)):
                    #     print(hex(f[i]))

            # TODO: I don't think we NEED an else error statement here, the only case that would cause
            #       that is reading the data line and both dstM and srcM are 00000000
    print(counter)


d = {
    "block_size": 16,
    "tag_size": 17,
    "associativity": 8,
    "total_rows": 4096,
    "index_size": 11,
    "offset_size": 4,
    "set_fields": [16, 12, 4],
}
c = Cache(d)
# print(split_address("0C809767", d["tag_size"], d["index_size"]))

# print(bin(0x7C809767))
# for i in range(len(f)):
#     print(hex(f[i]))
simulate(c, d, "Trace1half.trc")
