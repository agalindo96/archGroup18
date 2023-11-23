import math

from main import UNITS, ADDRESS_LENGTH, COST_PER_KB

# Performs the necessary calculations on the given arguments, pairs existing arg data values with descriptive keys 
def process_args(args) -> dict:
    # Convert cache size to bytes
    cache_size_bytes = args.s * UNITS["KB"]
    # Cache size divided by the total number of data bytes per row
    total_rows = cache_size_bytes // (args.a * args.b)
    # Size of the index in terms of bits
    index_size = int(math.log2(total_rows))
    # Size of the block offset in terms of bits
    offset_size = int(math.log2(args.b))
    # Size of the tag in terms of bits
    tag_size = ADDRESS_LENGTH - index_size - offset_size
    # +1 comes from the valid bit, divide by 8 to convert from bits to bytes
    overhead_size = ((tag_size + 1)  * args.a * total_rows) // 8
    # Stored in bytes for now, going to add units when printing
    total_memory_size = overhead_size + cache_size_bytes

    data = {
        # 1 KB - 8,192 KB
        "cache_size": args.s,
        # 4 bytes - 64 bytes
        "block_size": args.b,
        # [1, 2, 4, 8, 16]
        "associativity": args.a,
        # Translate shortened input to the full policy name
        "replacement_policy": "Random" if args.r == "RND" else "Round-Robin",
        "total_blocks": cache_size_bytes // args.b,
        "tag_size": tag_size,
        "index_size": index_size,
        "offset_size": offset_size,
        "total_rows": total_rows,
        "overhead_size": overhead_size,
        "total_memory_size": total_memory_size,
        "physical_memory_size" : args.p,
        # Since implementation memory size is stored in bytes, convert to KB for cost calculation
        "cost": total_memory_size // UNITS["KB"] * COST_PER_KB,
        # List of bit lengths used to split address into relevant substrings
        "set_field_lengths" : [tag_size, index_size, offset_size],
        "trace_files": [file for file in args.f]
    }

    return data

# This function finds the largest possible unit that a string of bytes can be converted to
# It does so by iterating over the dictionary of units in reverse order (right to left) 
# until it finds a value that is less than or equal to the byte string 
#
#                      <------      <------      <------                                 
#   UNITS = {"KB": 2**10, "MB": 2**20, "GB": 2**30}
#
# The next() function 'ends' the iteration once we encounter the FIRST value that is <= the given byte string
#
# Ex. Cache size has an initial value of 8,192 KB, print_milestone_one() converts it to bytes before passing
#     So cache size = 8,388,608 B; it's smaller than 2**30, so we iterate once more and compare it to 2**20
#     2**20 = 1,048,576 B, which is SMALLER than our cache size, so we know our cache can be divided into MB.
#     We return a tuple containing two values: first, the byte string converted to the largest unit
#     (8,192 KB = 8 MB), then the second value is a string representing the unit itself: "MB"
#     The tuple is used to populate the relevant statements in print_milestone_one()
def dynamic_conversion(memory_size) -> tuple:
    unit = next(unit for unit, value in reversed(UNITS.items()) if value <= memory_size)

    return (memory_size / UNITS[unit], unit)

def print_milestone_one(data) -> None:
    # Cache memory is stored in KB, convert to bytes then pass to dynamic conversion method
    cache_size_tuple = dynamic_conversion(data["cache_size"] * UNITS["KB"])
    total_memory_tuple = dynamic_conversion(data["total_memory_size"])

    print("Cache Simulator CS 3853 Fall 2023 - Group #18\n")

    for file in data["trace_files"]:
        print(f"Trace File: {file}\n\n***** Cache Input Parameters *****\n"
              f"{'Cache Size:':32}{int(cache_size_tuple[0])} {cache_size_tuple[1]}\n"
              f"{'Block Size:':32}{data['block_size']} bytes\n"
              f"{'Associativity:':32}{data['associativity']}\n"
              f"{'Replacement Policy:':32}{data['replacement_policy']}\n\n\n***** Cache Calculated Values *****\n\n"
              f"{'Total # Blocks:':32}{data['total_blocks']}\n"
              f"{'Tag Size:':32}{data['tag_size']} bits\n"
              f"{'Index Size:':32}{data['index_size']} bits\n"
              f"{'Total # Rows:':32}{data['total_rows']}\n"
              f"{'Overhead Size:':32}{data['overhead_size']} bytes\n"
              f"{'Implementation Memory Size:':32}{total_memory_tuple[0]:.2f} {total_memory_tuple[1]} ({data['total_memory_size']} bytes)\n"
              f"{'Cost:':32}${data['cost']:.2f} @ ($0.09 / KB)\n"
              )
# TODO: I guess the simulator function should iterate over the files, then call this print when it has the results?
def print_milestone_two(data) -> None:
    print(f"\n***** CACHE SIMULATION RESULTS *****\n\n"
          f"{'Total Cache Accesses:':27}######\n"
          f"{'Cache Hits:':27}######\n"
          f"{'Cache Misses:':27}####\n"
          f"{'--- Compulsory Misses:':27}####\n"
          f"{'--- Conflict Misses:':27}##\n\n"
          f"***** *****  CACHE HIT & MISS RATE:  ***** *****\n\n"
          f"{'Hit Rate:':24}##.####%\n"
          f"{'Miss Rate:':24}#.####%\n"
          f"{'CPI:':24}#.## Cycles/Instruction\n\n"
          f"{'Unused Cache Space:':24}###.## KB / ###.## KB = ##.##% Waste: $##.##\n"
          f"{'Unused Cache Blocks:':24}##### / #####\n\n"
          )
