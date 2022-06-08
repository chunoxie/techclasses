import ctypes

class DynamicArray:
    def __init__(self):
        self.count = 0
        self.capacity = 1
        self.current_array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def __getitem__(self, idx):
        if idx == -1: return self.current_array[self.count - 1]
        if not 0 <= idx < self.count:
            return IndexError('Index is out of bounds!')

        return self.current_array[idx]

    def append(self, item):
        # check if capacity has reached limit and resize array
        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        self.current_array[self.count] = item
        self.count += 1

    def _resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.current_array[i]
        
        self.current_array = new_array
        self.capacity = new_capacity

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()
