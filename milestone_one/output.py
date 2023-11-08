def print_out(args):
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
        print(f"{'Total # Blocks: ':32}#####")
        print(f"{'Tag Size: ':32}## bits")
        print(f"{'Index Size: ':32}## bits")
        print(f"{'Total # Rows: ':32}####")
        print(f"{'Overhead Size: ':32}##### bytes")
        print(f"{'Implementation Memory Size: ':32}###.## #B (###### bytes)")
        print(f"{'Cost: ':32}$##.## @ ($0.09 / KB)\n")
