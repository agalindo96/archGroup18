import argparse
import re

import parse_trace
import output

"""
    Figure how to structure this. Create executable?

    TODO: If we make an executable, change the program name in the usage statement
"""

units = {"KB": 2**10, "MB": 2**20, "GB": 2**30}

def parse_arguments():
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
        "-a", type=int, choices=[1, 2, 4, 8, 16], help="cache associativity", required=True
    )
    required_args.add_argument(
        "-r", choices=["RR", "RND"], help="replacement policy, either round-robin or random", required=True
    )
    required_args.add_argument(
        "-p",
        help="denotes the size of physical memory in KB from 64KB to 512GB",
        metavar="[64KB, 512GB]",
        required=True
    )

    args = parser.parse_args()

    physical_memory = parse_mem_string(args.p, parser)
    upper_range = int(512 * units["GB"] / units["KB"])

    if len(args.f) == 0 or len(args.f) > 3:
        parser.error(
            "File quantity error: Provide at least one, at most three filename arguments"
        )

    if args.s < 1 or args.s > 8192:
        parser.error("Cache size flag -s must be an integer value from 1 to 8192")

    if args.b < 4 or args.b > 64:
        parser.error("Block size flag -b must be an integer value from 4 to 64")

    if physical_memory < 64 or physical_memory > upper_range:
        parser.error(
            "Physical memory flag -p must be a string representing a memory size from 64 KB to 512 GB"
        )
        
    return args

"""
    Translates physical memory string input into the actual value in KB
    Used to validate if input is between 64KB and 512GB

    Ex. 8MB -> 8,192(KB)
"""
def parse_mem_string(str, parser):
    str = re.sub(r"([KMG]?B)", r" \1", str)

    try:
        number, unit = [string.strip() for string in str.split()]
    except:  # Handles if a number is provided without units
        parser.error("Physical memory argument must include units {KB, MB, GB}")

    return int(float(number) * units[unit] / units["KB"])

def main():
    args = parse_arguments()
    args.f = parse_trace.validate(args.f)
    if len(args.f) >= 1: output.print_results(args)

if __name__ == '__main__':
    main()
