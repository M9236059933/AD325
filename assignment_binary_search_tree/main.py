from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # helper function to insert a value into the BST
        def _insert(node, value):
            # base case: if the current node is None, insert the new value
            if not node:
                return TreeNode(value)
            # if the value is less than the current node's value, go left
            if value < node.value:
                # recursively insert into the left subtree
                node.left = _insert(node.left, value)
            # if the value is greater than the current node's value, go right
            elif value > node.value:
                # recursively insert into the right subtree
                node.right = _insert(node.right, value)
            # return current node up the recursion stack
            return node
        # insert the value starting from the root
        self.root = _insert(self.root, value)

    def search(self, value):
        # helper function to search for a value in the BST
        def _search(node, value):
            # base case: if the current node is None, value is not found
            if not node:
                return False
            # if the current node's value matches the search value, return True
            if node.value == value:
                return True
            # if the search value is less than the current node's value, search left 
            # otherwise, search right
            return _search(node.left, value) if value < node.value else _search(node.right, value)
        # start the checking from the root
        return _search(self.root, value)

    def delete(self, value):
        # helper function to find the minimum value node in a subtree
        def _min_value_node(node):
            # keep going left until we find the leftmost node
            while node.left:
                node = node.left
            return node
        # helper function to delete a value from the BST
        def _delete(node, value):
            # base case: if the current node is None, value is not found
            if not node:
                return None
            # if the value is less than the current node's value, go left
            if value < node.value:
                # recursively delete from the left subtree
                node.left = _delete(node.left, value)
            # if the value is greater than the current node's value, go right
            elif value > node.value:
                # recursively delete from the right subtree
                node.right = _delete(node.right, value)
            # if the value matches the current node's value
            else:
                # if node has no left child, return right child
                if not node.left:
                    return node.right
                # if node has no right child, return left child
                if not node.right:
                    return node.left
                
                # if node has two children, find the inorder successor (smallest in the right subtree)
                temp = _min_value_node(node.right)
                # replace the current node's value with the inorder successor's value
                node.value = temp.value
                # delete the inorder successor from the right subtree
                node.right = _delete(node.right, temp.value)
            # return the current node after deletion    
            return node
        # start the deletion from the root
        self.root = _delete(self.root, value)

    def inorder_traversal(self):
        # helper function to perform inorder traversal
        def _inorder(node):
            if node is None:
                return []
            # inorder traversal: left -> root -> right
            return _inorder(node.left) + [node.value] + _inorder(node.right)
        # start the traversal from the root
        return _inorder(self.root)
    