from collections import deque


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root is None:
        return []
    # preorder traversal: root -> left -> right
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def inorder_traversal(root):
    if root is None:
        return []
    # inorder traversal: left -> root -> right
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return []
    # postorder traversal: left -> right -> root
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]


def level_order_traversal(root):
    if root is None:
        return []
    # we use a deque for efficient pop from the left
    # initialize the queue with the root node
    queue = deque([root])

    # this will hold the result of the level order traversal
    result = []

    # while there are nodes to process
    while queue:
        # pop the leftmost node from the queue
        node = queue.popleft()

        # append the value of the node to the result
        result.append(node.val)

        # if the node has a left child, add it to the queue
        if node.left:
            queue.append(node.left)

        # if the node has a right child, add it to the queue
        if node.right:
            queue.append(node.right)
    
    return result

# most easy way to restore tree from preorder and inorder traversal
def build_tree_from_pre_in(preorder, inorder):

    # base case: if either list is empty, return None
    if not preorder or not inorder:
        return None
    
    # the first element of preorder is the root always
    root_val = preorder[0]

    # create the root node
    root = TreeNode(root_val)

    # find the index of the root in inorder to split left and right subtrees
    mid = inorder.index(root_val)

    # split the inorder list into left and right subtrees excluding the root
    left_subtree_inorder = inorder[:mid]
    right_subtree_inorder = inorder[mid+1:]

    # we skip the first element of preorder (the root) and take the next
    # amount of nodes in the left subtree is equal to the length of left_subtree_inorder
    # so we take the next mid elements for the left subtree
    left_subtree_preorder = preorder[1:1+mid]

    # the rest of the preorder list is the right subtree
    right_subtree_preorder = preorder[1+mid:]

    # recursively build the left and right subtrees
    root.left = build_tree_from_pre_in(left_subtree_preorder, left_subtree_inorder)
    root.right = build_tree_from_pre_in(right_subtree_preorder, right_subtree_inorder)

    return root


# function to print the tree structure in a readable format
def print_tree(node, level=0, indent_size=4):
    if node is not None:
        print_tree(node.right, level + 1, indent_size)
        print(" " * (level * indent_size) + "-- " + str(node.val))
        print_tree(node.left, level + 1, indent_size)