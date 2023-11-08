import decimal
import math

def print_out(args):
    total_blocks = (args.s * 1024) // args.b
    tag_size = 32 - int(math.log2(args.b)) - int(math.log2(total_blocks // args.a))
    index_size = int(math.log2(total_blocks // args.a))
    total_rows = total_blocks // args.a
    overhead_size = ((tag_size + 1) * args.a * total_rows) // 8
    #TODO: Need units, float precision, value in bytes
    memory_size = (overhead_size + args.s * 1024) / 1024.00
    cost = memory_size * 0.09

    replacement = "Random" if args.r == "RND" else "Round-Robin"

    print("Cache Simulator CS 3853 Fall 2023 - Group #18\n")

    for file in args.f:
        print(f"Trace File: {file}\n")
        print("***** Cache Input Parameters *****")
        print(f"{'Cache Size: ':32}{args.s} KB")
        print(f"{'Block Size: ':32}{args.b} bytes")
        print(f"{'Associativity: ':32}{args.a}")
        print(f"{'Replacement Policy: ':32}{replacement}\n\n")

        print("***** Cache Calculated Values *****\n")
        print(f"{'Total # Blocks: ':32}{total_blocks}")
        print(f"{'Tag Size: ':32}{tag_size} bits")
        print(f"{'Index Size: ':32}{index_size} bits")
        print(f"{'Total # Rows: ':32}{total_rows}")
        print(f"{'Overhead Size: ':32}{overhead_size} bytes")
        print(f"{'Implementation Memory Size: ':32}{memory_size:.2f} KB ({int(memory_size * math.pow(2, 10))} bytes)")
        print(f"{'Cost: ':32}${cost:.2f} @ ($0.09 / KB)\n")
