def print_out(args):
    replacement = "Random" if args.r == "RND" else "Round-Robin"

    print("Cache Simulator CS 3853 Fall 2023 - Group #18\n")

    for file in args.f:
        print(f"Trace File: {file}\n")
        print("***** Cache Input Parameters *****")
        print(f"Cache Size:\t\t\t{args.s} KB")
        print(f"Block Size:\t\t\t{args.b} bytes")
        print(f"Associativity:\t\t\t{args.a}")
        print(f"Replacement Policy:\t\t{replacement}\n\n")

        print("***** Cache Calculated Values *****\n")
        print(f"Total # Blocks:\t\t\t#####")
        print(f"Tag Size:\t\t\t## bits")
        print(f"Index Size:\t\t\t## bits")
        print(f"Total # Rows:\t\t\t####")
        print(f"Overhead Size:\t\t\t##### bytes")
        print(f"Implementation Memory Size:\t###.## #B (###### bytes)")
        print(f"Cost:\t\t\t\t$##.## @ ($0.09 / KB)\n")

