from set import Set

class Cache:
    # Represents a Cache comprised of many Sets
    def __init__(self, data):
        self.sets = [Set(data["block_size"]) for i in range(data["total_rows"])]

    def __repr__(self):
        return f"Set: {self.sets}"