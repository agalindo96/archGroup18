import argparse
import re

import parse_trace
import output

"""
    Figure how to structure this. Create executable?

    TODO: If we make an executable, change the program name in the usage statement
"""

# Powers of 2 corresponding to the values of KB, MB, and GB in terms of bytes
UNITS = {"KB": 2**10, "MB": 2**20, "GB": 2**30}

# Length of addresses in terms of bits
ADDRESS_LENGTH = 32

# All possible associativity options for this simulation
ASSOCIATIVITY = [1, 2, 4, 8, 16]

# Block size bounds in terms of bytes
B_SIZE_LOWER = 4
B_SIZE_UPPER = 64

# Cache size bounds in terms of KB
C_SIZE_LOWER = 1
C_SIZE_UPPER = int(8 * UNITS["MB"] / UNITS["KB"])

# Average cost to implement a KB of cache memory
COST_PER_KB = 0.09

# The maximum number of input trace files
MAX_NUM_FILES = 3

# Physical memory bounds in terms of bytes
# Note: We will process '-p' arguments as strings to spare the user
#       from having to type large memory values in terms of KB
#           Ex: 512 GB = 536,870,912 KB
P_MEM_LOWER = 64 * UNITS["KB"]
P_MEM_UPPER = 512 * UNITS["GB"]

# Cache block replacement policies, either Round-Robin or Random
R_POLICIES = ["RR", "RND"]

'''
    argparse.parse_args() returns a 'Namespace' object, similar to a list, accessed with dot notation
    The returned Namespace will contain all the arguments provided by the user
    https://realpython.com/command-line-interfaces-python-argparse/#parsing-command-line-arguments-and-options
'''
def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    required_args = parser.add_argument_group('required arguments')

    required_args.add_argument(
        "-f",
        action="append",
        default=[],
        metavar="filename",
        help="name of text file with the trace",
        required=True
    )
    required_args.add_argument(
        "-s",
        type=int,
        metavar="[1, 8192]",
        help="denotes the cache size in KB from 1KB to 8MB",
        required=True
    )
    required_args.add_argument(
        "-b",
        type=int,
        metavar="[4, 64]",
        help="denotes the block size in B from 4B to 64B",
        required=True
    )
    required_args.add_argument(
        "-a", type=int, choices=ASSOCIATIVITY, help="cache associativity", required=True
    )
    required_args.add_argument(
        "-r", choices=R_POLICIES, help="replacement policy, either round-robin or random", required=True
    )
    required_args.add_argument(
        "-p",
        help="denotes the size of physical memory in KB from 64KB to 512GB",
        metavar="[64KB, 512GB]",
        required=True
    )

    args = parser.parse_args()

    physical_memory = parse_mem_string(args.p, parser)

    if len(args.f) == 0 or len(args.f) > MAX_NUM_FILES:
        parser.error(
            "File quantity error: Provide at least one, at most three filename arguments"
        )
    
    if args.s < C_SIZE_LOWER or args.s > C_SIZE_UPPER:
        parser.error("Cache size flag -s must be an integer value from 1 to 8192")

    if args.b < B_SIZE_LOWER or args.b > B_SIZE_UPPER:
        parser.error("Block size flag -b must be an integer value from 4 to 64")

    if physical_memory < P_MEM_LOWER or physical_memory > P_MEM_UPPER:
        parser.error(
            "Physical memory flag -p must be a string representing a memory size from 64 KB to 512 GB"
        )
        
    return args

"""
    Translates physical memory string argument to the actual byte value and returns that integer
    This allows us to compare the entered memory value with the predefined boundaries
    Returning the value in bytes lets this function work for KB, MB, and GB

    Ex. 8MB -> 8,192(KB)
"""
def parse_mem_string(str, parser) -> int:
    # Adds a space between the number and the unit
    str = re.sub(r"([KMG]?B)", r" \1", str)

    try:
        # Splits on whitespace and assigns the number and unit values to variables
        number, unit = [string.strip() for string in str.split()]
    except:  # Handles if a number is provided without units
        parser.error("Physical memory argument must include units {KB, MB, GB}")

    return int(number) * UNITS[unit]

def main() -> None:
    # Parse the user input, get a list-like object containing all the arguments
    args = parse_arguments()

    # Call external validation function. Verifies that the files entered exist.
    # Overwrites the existing field for file arguments with a list of all valid files
    args.f = parse_trace.validate(args.f)

    # If the user provided at least one valid file name
    if len(args.f) >= 1:
        arg_data = output.process_args(args)
        output.print_milestone_one(arg_data)
    else: # None of the files were valid
        print(print(f"Failed to find any existing files."))
        exit()

if __name__ == '__main__':
    main()
