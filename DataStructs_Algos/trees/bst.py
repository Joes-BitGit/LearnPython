class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_val(self.root, new_val)

    def search(self, find_val):
        return self.search_val(self.root, find_val)

    def insert_val(self, start, new_val):
        if start.value < new_val:
            if start.right:
                self.insert_val(start.right, new_val)
            else:
                start.right = Node(new_val)
        else:
            if start.left:
                self.insert_val(start.left, new_val)
            else:
                start.left = Node(new_val)

    def search_val(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif start.value > find_val:
                return self.search_val(start.left, find_val)
            else:
                return self.search_val(start.right, find_val)
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
