class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()


def build_tree(elements):
    print("Elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    Name = ["Y","L","I", "Z","A", "N", "I", "C", "O", "L", "E", "R", "E", "Q", "U", "I", "L", "L", "A", "S", "S", "A","L", "A", "Z", "A", "R"]
    name_tree = build_tree(Name)


print("Min: ", name_tree.find_min())
print("Max:",name_tree.find_max())