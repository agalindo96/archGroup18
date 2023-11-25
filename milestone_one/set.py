class Set:
    # Represents a set (row) in the cache

    '''
        What is the best way to determine if a block is full?
        Would adding a variable to indicate that contribute to overhead?
        Or would we just ignore that in our calculations?
    '''
    def __init__(self, size):
        self.valid = 0
        self.tag = 0
        self.data = [0] * size