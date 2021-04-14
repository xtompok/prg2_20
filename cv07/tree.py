class BST(object):
    """ Class for handling binary search tree """
    def __init__(self):
        self.root=None
    
    def insert(self,num):
        # Pokud je root None, vyrob Node uloženým num
        if self.root is None:
            self.root = Node(num)
        # Jinak zavolej insert na root
        else:
            self.root.insert(num)

class Node(object):
    """ One binary search tree node """
    def __init__(self,data):
        self.data = data    # Data stored in node (currently int)
        self.depth = 0      # depth of the subtree with self as root (for AVL debug)
        self.delta = 0      # difference between depth of the right and the left subtree (for AVL)
        self.left = None    # Left child
        self.right = None   # Right child
        self.up = None      # Parent

    def __str__(self):
        # Node has both children
        if self.left is not None and self.right is not None:
            return f"Node({self.data}, {id(self)}): up:{id(self.up)}, left: {self.left.data}-{id(self.left)}, right: {self.right.data}-{id(self.right)}"
        # Node has only left child
        if self.left is not None:
            return f"Node({self.data}, {id(self)}): up:{id(self.up)}, left: {self.left.data}-{id(self.left)}, right: None"
        # Node has only right child
        if self.right is not None:
            return f"Node({self.data}, {id(self)}): up:{id(self.up)}, left: None, right: {self.right.data}-{id(self.right)}"
        # Node has no child
        return f"Node({self.data}, {id(self)}): up:{id(self.up)}, left: None, right: None"
        #return "Node({}, {}): up: {}, left:...".format(self.data,id(self), id(self.up))

    def insert(self,num):
        # num already in the tree
        if self.data == num:
            return
        
        # num is smaller than the number in the current node -> go left
        if num < self.data:
            # we have no left son -> create one and return
            if self.left is None:
                self.left = Node(num)
                self.left.up = self
                return
            # we have left son -> recurse to the left son
            else:
                self.left.insert(num)
        # num is greater than the number in the current node -> go right
        else:
            # we have no right son -> create one and return
            if self.right is None:
                self.right = Node(num)
                self.right.up = self
            # we have left son -> recurse to the right
            else:
                self.right.insert(num)


    def rot_right(self):
        # Rotate edge to the right son
        x = self
        y = self.right
        b = y.left
        if b is None:
            b = Node(-1000) 
            b.up = y

        if x.up is None:
            x.right = y.left
            y.left = x
            return y

        if x.up.left == self: # we are left son
            print("Left son")
            tmp = x.up.left
            x.up.left = x.right
            x.right = y.left
            y.left = tmp
        elif x.up.right == self: # else; we are right son
            print("Right")
            tmp = x.up.right
            x.up.right = x.right
            x.right = y.left
            y.left = tmp

        tmp  = x.up
        x.up = b.up
        b.up = y.up
        y.up = tmp


        


n = Node(1)
n2 = Node(1)

bst = BST()
bst.insert(10)
bst.insert(8)
bst.insert(11)
bst.insert(9)



bst.root = n
for i in range(2,6):
    n.right = Node(i)
    n.right.up = n
    print(n)
    n = n.right

two = bst.root.right
print("Before:")
print(two)
print(two.right)
two.rot_right()
print("After")
print(bst.root.right)
print(bst.root.right.left)
print(bst.root.right.right)




