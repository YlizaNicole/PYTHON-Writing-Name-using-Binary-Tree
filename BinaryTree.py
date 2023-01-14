# https://www.youtube.com/watch?v=lFq5mYUWEBk as guide


Menu= print("========MENU========")
print ("| [1] = Search      |")
print ("| [2] = Exit        |")
print("====================")



while True:
    print()
    user_input= int(input("pick a number: "))
    if user_input ==1:
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


            def search(self, val):
                if self.data == val:
                    return True

                if val < self.data:
                    if self.left:
                        return self.left.search(val)
                    else:
                        return False

                if val > self.data:
                    if self.right:
                        return self.right.search(val)
                    else:
                        return False




        def build_tree(elements):
            root = BinarySearchTreeNode(elements[0])

            for i in range(1,len(elements)):
                root.add_child(elements[i])

            return root

        if __name__ == '__main__':
            FullName = ["Y","L","I", "Z","A", "N", "I", "C", "O", "L", "E", "S", "A","L", "A", "Z", "A", "R" ]
            FullName_tree = build_tree(FullName)

            print ("Enter the LETTER you want to find:")

            User_Input = input("")
            Uppercased = User_Input.upper()
            print("in the list? ", FullName_tree.search(Uppercased))

    if user_input==2:
        question= input("exit? (y/n)")
        if question == "y":
            print("bye bye :>")
        break
