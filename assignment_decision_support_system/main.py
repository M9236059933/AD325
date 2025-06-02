class Node:
    def __init__(self, question):
        self.question = question
        self.left = None  # Yes
        self.right = None # No

def max_depth(root):
    # If the node is null, we've reached the bottom of the tree
    if not root:
        return 0

    # Recursively compute the depth of each subtree
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # The depth at the current node is 1 plus the max of both sides
    return 1 + max(left_depth, right_depth)