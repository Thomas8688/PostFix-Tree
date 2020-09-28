#Postfix Notation Tree Solution, using Stacks
#Node class which will be used to create the subtrees on the stack

#CLASSES & FUNCTIONS

class Node:
#Sets up the class to allow for recursion
    def __init__(self, value):
        self._value = value
        self._right = None
        self._left = None

#Procedure to give the left node a value
    def addLeft(self, value):
        self._left = value

#Procedure to give the right node a value
    def addRight(self, value):
        self._right = value

#Procedure that prints the tree through post order traversal (Postfix Notation)
    def postOrderTraversal(self):
#Checks that the left node exists
        if self._left:
#Checks if the left node is a subtree root or a leaf node
            if isinstance(self._left, str):
                print(self._left)
            else:
#If the left is not a leaf node, recursion is used to traverse the left subtree
                self._left.postOrderTraversal()
#Checks that the right node exists
        if self._right:
#Checks if the right node is a subtree root or a leaf node
            if isinstance(self._right, str):
                print(self._right)
            else:
#If the right is not a leaf node, recursion is used to traverse the right subtree
                self._right.postOrderTraversal()
#Prints the node value at the end
        print(self._value)

#Procedure the prints the tree through in order traversal (Infix notation)
    def inOrderTraversal(self):
#SAME AS postOrderTraversal(), but the node value is printed between the left and right
        print("()")
        if self._left:
            if isinstance(self._left, str):
                print(self._left)
            else:
                self._left.inOrderTraversal()
        print(self._value)
        if self._right:
            if isinstance(self._right, str):
                print(self._right)
            else:
                self._right.inOrderTraversal()
        print(")")

#Function to check if a value is an operand or an operator
def operand(value):
    if value not in ["+","-", "*", "/"]:
        return True
    else:
        return False

#Procedure used to convert a postfix notation list into a tree  (*USING STACKS)
def treeCreater(postfix):
#Creates the stack
    stack = []
#Sets up the while loop, and index counter
    loop = True
    i = 0
    while loop:
#If the index value is an operand, it is immediately added to the tree
        if operand(postfix[i]):
            stack.append(postfix[i])
#Otherwise, the first two values are taken from the stack
        else:
            right = stack.pop()
            left = stack.pop()
#And a tree is created with the operator in the middle
            adder = Node(postfix[i])
            adder.addLeft(left)
            adder.addRight(right)
            stack.append(adder)
#The index counter is increased
        i += 1
#Checks if the loop needs to be terminated
        if i >= len(postfix):
             loop = False
    return stack


#Function used to create a tree
def createTree(string):
#Splits the string into a list of the values seperated by spaces
    string = string.split(' ')
    print ("Creating...\n")
#Creates the tree using the function above
    mytree = treeCreater(string)
    print("Created!\n")
    return (mytree)

#Procedure used to print the tree in postfix form
def showPostfix(tree):
    print("Traversing...\n")
#Goes through each item in the tree
    for item in tree:
#If the item is a leaf node, the item is immediately printed
        if isinstance(item, str):
            print (item)
        else:
#Otherwise, the subtree is traversed
            item.postOrderTraversal()
    print("\nTraversed!\n")

#Procedure used to print the tree in infix form
def showInfix(tree):
    print("Traversing...\n")
#Same method as above, however uses the inOrderTraversal procedure instead
    for item in tree:
        if isinstance(item, str):
            print(item)
        else:
            item.inOrderTraversal()
    print("\nTraversed!\n")


#TESTING

myPostfix = "5 6 3 * 2 - +"
myPostfix2 = "100 7 3 1 - * 6 + - 10 +"
myPFT = createTree(myPostfix2)
showPostfix(myPFT)
showInfix(myPFT)
print("checker")
