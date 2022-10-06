class BinaryTree:
    def __init__(self, code, price):
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def insert(self, code, price):
        if not isinstance(code, int):
            raise TypeError("Item code should be an integer type value!")

        if not isinstance(price, (int, float)):
            raise TypeError("Items price should be an integer or float value!")

        if not self.code:
            self.code = code
            self.price = price
            return

        if code < self.code:
            if self.left:
                self.left.insert(code, price)
                return

            self.left = BinaryTree(code, price)
            return

        if self.right:
            self.right.insert(code, price)
            return

        self.right = BinaryTree(code, price)

    def find(self, code, volume):
        if not isinstance(volume, int):
            raise TypeError("Volume of items should be integer type value!")

        if code == self.code:
            return self.price * volume

        if code < self.code:
            if self.left:
                return self.left.find(code, volume)

        else:
            if self.right:
                return self.right.find(code, volume)

        raise ValueError("Searched code doesnt exist in this tree")


def main():
    root = BinaryTree(25, 19.7)
    root.insert(17, 21)
    root.insert(9, 12)
    root.insert(32, 28.5)
    root.insert(10, 37)
    print(root.find(2, 15))
    print(root.find(18, 2))


if __name__ == '__main__':
    main()