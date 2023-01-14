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

    def calculate_sum(self):
        sum = self.data
        if self.left:
            sum += self.left.calculate_sum()
        if self.right:
            sum += self.right.calculate_sum()
        return sum
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
        
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements


        
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
print("Sum:", name_tree.calculate_sum())
print("In order traversal:", name_tree.in_order_traversal())
print("Pre order traversal:", name_tree.pre_order_traversal())
print("Post order traversal:", name_tree.post_order_traversal())