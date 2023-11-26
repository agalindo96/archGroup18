import math
import re

from cache import Cache
from set import Set

def main() -> None:
    address = 0x7c809767
    offset_bits = 4
    index_bits = 12
    tag_bits = 16
    # TODO: Make an array of bit lengths for index, tag, and offset - in that order
    str = "7c809767"
    d = {"block_size": 4, "tag_size": 8, "associativity": 2, "total_rows": 64}
    c = Cache(d)
    s = Set(d)
    print(s.valid, "\n",  s.tag, "\n", s.data)
    print(len(s.valid))
    #print(shift)
    # tag = address[0:int(math.log2(tag_bits))]
    # index = address[int(math.log2(tag_bits):int(math.log2(index_bits)]
    #print(tag)
if __name__ == '__main__':
    main()
