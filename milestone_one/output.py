import decimal
import math

def print_results(args):
    total_blocks = (args.s * 1024) // args.b
    tag_size = 32 - int(math.log2(args.b)) - int(math.log2(total_blocks // args.a))
    index_size = int(math.log2(total_blocks // args.a))
    total_rows = total_blocks // args.a
    overhead_size = ((tag_size + 1) * args.a * total_rows) // 8
    memory_size = (overhead_size + args.s * 1024) / 1024.00
    cost = memory_size * 0.09

    replacement = "Random" if args.r == "RND" else "Round-Robin"

    print("Cache Simulator CS 3853 Fall 2023 - Group #18\n")

    for file in args.f:
        # print(f"Trace File: {file}\n")
        # print("***** Cache Input Parameters *****")
        # print(f"{'Cache Size: ':32}{args.s} KB")
        # print(f"{'Block Size: ':32}{args.b} bytes")
        # print(f"{'Associativity: ':32}{args.a}")
        # print(f"{'Replacement Policy: ':32}{replacement}\n\n")

        # print("***** Cache Calculated Values *****\n")
        # print(f"{'Total # Blocks: ':32}{total_blocks}")
        # print(f"{'Tag Size: ':32}{tag_size} bits")
        # print(f"{'Index Size: ':32}{index_size} bits")
        # print(f"{'Total # Rows: ':32}{total_rows}")
        # print(f"{'Overhead Size: ':32}{overhead_size} bytes")
        # print(f"{'Implementation Memory Size: ':32}{memory_size:.2f} KB ({int(memory_size * math.pow(2, 10))} bytes)")
        # print(f"{'Cost: ':32}${cost:.2f} @ ($0.09 / KB)\n")

        print(f"Trace File: {file}\n\n***** Cache Input Parameters *****\n"
              f"{'Cache Size:':32}{args.s} KB\n"
              f"{'Block Size:':32}{args.b} bytes\n"
              f"{'Associativity:':32}{args.a}\n"
              f"{'Replacement Policy:':32}{replacement}\n\n\n***** Cache Calculated Values *****\n\n"
              f"{'Total # Blocks:':32}{total_blocks}\n"
              f"{'Tag Size:':32}{tag_size} bits\n"
              f"{'Index Size:':32}{index_size} bits\n"
              f"{'Total # Rows:':32}{total_rows}\n"
              f"{'Overhead Size:':32}{overhead_size} bytes\n"
              f"{'Implementation Memory Size:':32}{memory_size:.2f} KB ({int(memory_size * math.pow(2, 10))} bytes)\n"
              f"{'Cost:':32}${cost:.2f} @ ($0.09 / KB)\n")
        
        # How do we calculate unused cache blocks?
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
