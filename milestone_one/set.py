class Set:
    # Represents a set (row) in the cache

    '''
        What is the best way to determine if a block is full?
        Would adding a variable to indicate that contribute to overhead?
        Or would we just ignore that in our calculations?
    '''
    def __init__(self, data):
        self.valid = [0] * data["associativity"]
        self.tag = [[0 for i in range(data["tag_size"])] for j in range(data["associativity"])]
        self.data = [[0 for i in range(data["block_size"])] for j in range(data["associativity"])]