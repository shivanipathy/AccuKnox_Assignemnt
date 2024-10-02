class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(14, 4)

# Iterating over the instance
for dimension in rect:
    print(dimension)

#Output:
# {'length': 14}
# {'width': 4}

