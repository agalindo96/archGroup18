# This module defines project-level constants

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

# Length of a read/write to memory in bytes
DATA_ACCESS_LENGTH = 4

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