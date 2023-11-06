import argparse
import re

"""
    "Note that in my sample simulation, for cache size I only accept numbers,
    so for 8MB would have to put in “-s 8192”"

    We're gonna need to process physical memory size arg as a string since the upper range 
    would be way too long to manually enter (512GB = 536,870,912KB)

    To validate we're gonna have to translate the arg to an integer and compare against the lower/upper range
"""

"""
    Figure how to structure this. Create executable? Driver script? 
"""

units = {"KB": 2**10, "MB": 2**20, "GB": 2**30}


def parse_mem_string(str):
    str = re.sub(r"([KMGT]?B)", r" \1", str)

    try:
        number, unit = [string.strip() for string in str.split()]
    except:
        parser.error("Physical memory argument must include units (Ex. 128MB)")

    return int(float(number) * units[unit] / units["KB"])


parser = argparse.ArgumentParser()

parser.add_argument("-f", action="append")
cache_size = parser.add_argument(
    "-s",
    type=int,
    metavar="[1, 8192]",
    help="denotes the cache size in KB from 1 KB to 8 MB",
)
block_size = parser.add_argument(
    "-b",
    type=int,
    metavar="[4, 64]",
    help="denotes the block size in B from 4 B to 64 B",
)
parser.add_argument(
    "-a", type=int, choices=[1, 2, 4, 8, 16], help="cache associativity"
)
parser.add_argument(
    "-r", choices=["RR", "RND"], help="replacement policy, either round-robin or random"
)
parser.add_argument(
    "-p",
    help="denotes the size of physical memory in KB from 64 KB to 512 GB",
)

args = parser.parse_args()
physical_memory = parse_mem_string(args.p)
upper_range = int(512 * units["GB"] / units["KB"])

if args.s < 0 or args.s > 8192:
    parser.error("Cache size flag -s must be an integer value from 1 to 8192")

if args.b < 4 or args.b > 64:
    parser.error("Block size flag -b must be an integer value from 4 to 64")

if physical_memory < 64 or physical_memory > upper_range:
    parser.error(
        "Physical memory flag -p must be a string representing a memory size from 64 KB to 512 GB"
    )


print(args)
