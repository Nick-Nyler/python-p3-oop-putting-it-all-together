# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if isinstance(new_size, int):
            self._size = new_size
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"