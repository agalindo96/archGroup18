import random
import re

from set import Set
#from . import constants

class Cache:
    # Represents a Cache comprised of many Sets
    def __init__(self, data):
        self.sets = [Set(data) for i in range(data["total_rows"])]

    def __repr__(self):
        return f"Set: {self.sets}"
    
    # TODO: Make sure this is right
    def random_replace(self, cacheSet):
        for testSet in self.sets:
            if testSet == cacheSet:
                validLength = len(testSet.valid)
                randomVal = random.randint(0, validLength - 1)
        return randomVal

# TEST
# d = {"block_size": 4, "tag_size": 8, "associativity": 2, "total_rows": 64}
# c = Cache(d)
# c.simulate(d, 'Trace1.trc')