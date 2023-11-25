import math
import re

from cache import Cache

def main() -> None:
    address = 0x7c809767
    offset_bits = 4
    index_bits = 12
    tag_bits = 16
    # TODO: Make an array of bit lengths for index, tag, and offset - in that order
    str = "7c809767"
    d = {"block_size": 4, "total_rows": 8}
    c = Cache(d)
    print(c)
    #print(shift)
    # tag = address[0:int(math.log2(tag_bits))]
    # index = address[int(math.log2(tag_bits):int(math.log2(index_bits)]
    #print(tag)
if __name__ == '__main__':
    main()
