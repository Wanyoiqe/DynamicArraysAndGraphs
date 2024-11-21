class DynamicArray:
    def __init__(self):
        self.array = []
        self.capacity = 1
        self.size = 0

    def insert(self, value):
        if self.size == self.capacity:
            self._resize()
        self.array.append(value)
        self.size += 1

    def _resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __str__(self):
        return str(self.array[:self.size])

# Simulation
posts = DynamicArray()
total_operations = 0

for i in range(1, 21):  # Insert 20 posts
    posts.insert(i)
    total_operations += 1

print("Dynamic Array:", posts)
print("Total Operations:", total_operations)
