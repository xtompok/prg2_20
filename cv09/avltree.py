class BST(object):
    """ Class for handling binary search tree """
    def __init__(self):
        self.root=None
    
    def insert(self,num: int)-> None:
        if self.root is None:
            self.root = Node(num)
        else:
            self.root = self.root.insert(num)
    
    
    def find(self,num: int)-> bool:
        """ Check if given number is in the tree. Returns True if it is, False otherwise. """
        if self.root is None:
            return False
        return self.root.find(num) # else is not needed, if ends with return

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
        if self.left is not None and self.right is not None:
            return f"Node({self.data}, {id(self)}): up:{id(self.up)}, left: {self.left.data}-{id(self.left)}, right: {self.right.data}-{id(self.right)}"
        if self.left is not None:
            return f"Node({self.data}, {id(self)}): up:{id(self.up)}, left: {self.left.data}-{id(self.left)}, right: None"
        if self.right is not None:
            return f"Node({self.data}, {id(self)}): up:{id(self.up)}, left: None, right: {self.right.data}-{id(self.right)}"
        return f"Node({self.data}, {id(self)}): up:{id(self.up)}, left: None, right: None"

    def insert(self,num):
        """ Insert number into AVL Tree.
        Returns root of self subtree """
        # Do nothing if number is already present
        if self.data == num:
            return self
        
        # Insert number into BST
        if num < self.data:
            if self.left is None:
                self.left = Node(num)
                self.left.up = self
            else:
                self.left.insert(num)
        else:
            if self.right is None:
                self.right = Node(num)
                self.right.up = self
            else:
                self.right.insert(num)
        
        # Calculate new value of the subtree depth
        if self.left:
            ldepth = self.left.depth + 1
        else:
            ldepth = 0
        if self.right:
            rdepth = self.right.depth + 1
        else:
            rdepth = 0
        
        # Calculate self depth
        self.depth = max(ldepth, rdepth)
        # Dopište určování self.delta
        self.delta = rdepth - ldepth
        print(self)
        print(self.delta)

        if self.delta == 2:
            if self.right.delta == 1:
                print("Right son delta 1")
                return self.rot_right()
            elif self.right.delta == -1:
                print("Right son delta -1")
                return self.rot_rl()
        elif self.delta == -2:
            if self.left.delta == 1:
                print("Left son delta 1")
                return self.rot_lr()
            elif self.left.delta == -1:
                print("Left son delta -1")
                return self.rot_left()

        return self

    def find(self,num: int)->bool:
        """ Recursively find element in the tree. Return True if it exists, False otherwise"""
        if self.data == num:
            return True
        if num < self.data:
            if self.left is None:
                return False
            return self.left.find(num)
        else:
            if self.right is None:
                return False
            return self.right.find(num)


    def rot_right(self):
        """ Rotate edge to the right son """
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

        return y

    def rot_left(self):
        """ Rotate edge to the right son """
        x = self
        y = self.left
        b = y.right
        if b is None:
            b = Node(-1000) 
            b.up = y

        if x.up is None:
            x.left = y.right
            y.right = x
            return y

        if x.up.right == self: # we are right son
            print("Left son")
            tmp = x.up.right
            x.up.right = x.left
            x.left = y.right
            y.right = tmp
        elif x.up.left == self: # else; we are left son
            print("Right")
            tmp = x.up.left
            x.up.left = x.left
            x.left = y.right
            y.right = tmp

        tmp  = x.up
        x.up = b.up
        b.up = y.up
        y.up = tmp

        return y
    
    def rot_lr(self):
        """ Double rotation, upper edge is to the left son"""
        z = self
        x = z.left
        y = x.right

        x.rot_right()
        z.rot_left()

        print(y)
        return y

    def rot_rl(self):
        """ Double rotation, upper edge is to the right son"""
        z = self
        x = z.right
        y = x.left

        x.rot_left()
        z.rot_right()

        print(y)
        return y


bst = BST()

bst.insert(3)
bst.insert(1)
bst.insert(2)

print(bst.root)

#bst.insert(10)
#bst.insert(8)
#bst.insert(11)
#bst.insert(9)
#print(bst.find(8))
#print(bst.find(10))
#print(bst.find(42))
