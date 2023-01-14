# https://www.youtube.com/watch?v=lFq5mYUWEBk as guide

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





if __name__ == '__main__':
    numbers= [17, 4, 1, 20, 9, 23, 18, 34]
    print (numbers)