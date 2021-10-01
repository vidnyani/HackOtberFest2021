class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BTree:
    def __init__(self):
        self.root = None
        self.temproot = None
    def insert(self, newdata):
        if self.root == None:
            self.root = newdata
        elif self.temproot:
            if newdata.data < self.temproot.data:
                if self.temproot.left == None:
                    self.temproot.left = newdata
                    self.temproot=None
                else:
                    self.temproot = self.temproot.left
                    self.insert(newdata)
            elif newdata.data > self.temproot.data:
                if self.temproot.right == None:
                    self.temproot.right = newdata
                    self.temproot=None
                else:
                    self.temproot = self.temproot.right
                    self.insert(newdata)
        elif self.root:
            if newdata.data < self.root.data:
                if self.root.left == None:
                    self.root.left = newdata
                elif self.root.left:
                    self.temproot = self.root.left
                    self.insert(newdata)
            elif newdata.data > self.root.data:
                if self.root.right == None:
                    self.root.right = newdata
                elif self.root.right:
                    self.temproot = self.root.right
                    self.insert(newdata)
    def preorder(self, temp):
        if temp != None:
            print(temp.data,",",end="")
            self.preorder(temp.left)
            self.preorder(temp.right)
    def inorder(self, temp):
        if temp != None:
            self.inorder(temp.left)
            print(temp.data,",",end="")
            self.inorder(temp.right)
    def postorder(self, temp):
        if temp != None:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data,",",end="")
BinaryTree = BTree()
while True:
    print("1.Insert")
    print("2.Preorder")
    print("3.Inorder")
    print("4.Postorder")
    print("5.Exit")
    choice = int(input("Enter the Choice : "))
    if choice == 1:
        element = int(input("Enter the Data : "))
        data = Node(element)
        BinaryTree.insert(data)
    elif choice == 2:
        BinaryTree.preorder(BinaryTree.root)
        print("")
    elif choice == 3:
        BinaryTree.inorder(BinaryTree.root)
        print("")
    elif choice == 4:
        BinaryTree.postorder(BinaryTree.root)
        print("")
    elif choice == 5:
        break






