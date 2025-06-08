from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Helper function to insert a value in the AVL tree
        def _insert(node, value):
            # Base case: if the tree is empty, return a new node
            if not node:
                return TreeNode(value)
            # if the value is less than the node's value, insert in the left subtree
            if value < node.value:
                node.left = _insert(node.left, value)
            # if the value is greater than the node's value, insert in the right subtree    
            elif value > node.value:
                node.right = _insert(node.right, value)
            # if the value is equal, do nothing (no duplicates allowed), return the node
            else:
                return node

            # Update the height of the ancestor node
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            # Get the balance factor of this ancestor node to check whether this node became unbalanced
            balance = self._get_balance(node)

            # If the node becomes unbalanced, then there are 4 cases to consider
            # Left Left Case
            if balance > 1 and value < node.left.value:
                return self._rotate_right(node)
            # Right Right Case
            if balance < -1 and value > node.right.value:
                return self._rotate_left(node)
            # Left Right Case
            if balance > 1 and value > node.left.value:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
            # Right Left Case
            if balance < -1 and value < node.right.value:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
            # Return the (unchanged) node pointer
            return node
        # Start the recursive insertion
        self.root = _insert(self.root, value)

    def delete(self, value):
        # Helper function  to find the node with the minimum value in a subtree
        def _min_value_node(node):
            # suppose the minimum value is node itself
            current = node
            # traverse the left subtree until we reach the leftmost node
            while current.left:
                current = current.left
            # return the leftmost node
            return current

        # Helper function to delete a node with the given value
        def _delete(node, value):
            # Base case: if the node is empty, return None
            if not node:
                return None
            # If the value is less than the node's value, go to the left subtree
            if value < node.value:
                node.left = _delete(node.left, value)
            # If the value is greater than the node's value, go to the right subtree
            elif value > node.value:
                node.right = _delete(node.right, value)
            # If the value is equal to the node's value, this is the node to be deleted
            else:
                # if left child is None, return the right child
                if not node.left:
                    return node.right
                # if right child is None, return the left child
                elif not node.right:
                    return node.left
                # if both children are present, find the minimum value node in the right subtree
                temp = _min_value_node(node.right)
                # Copy the value of the minimum node to the current node
                node.value = temp.value
                # Delete the minimum value node from the right subtree
                node.right = _delete(node.right, temp.value)


            # Update the height of the ancestor node
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            # Get the balance factor of this ancestor node to check whether this node became unbalanced
            balance = self._get_balance(node)

            # If the node becomes unbalanced, then there are 4 cases to consider
            # Left Left Case
            if balance > 1 and self._get_balance(node.left) >= 0:
                return self._rotate_right(node)
            # Right Right Case
            if balance > 1 and self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
            # Left Right Case
            if balance < -1 and self._get_balance(node.right) <= 0:
                return self._rotate_left(node)
            # Right Left Case
            if balance < -1 and self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
            # Return the (unchanged) node pointer
            return node
        # Start the recursive deletion
        self.root = _delete(self.root, value)

    def search(self, value):
        # Helper function to search for a value in the AVL tree
        def _search(node, value):
            # Base case: if the node is None, return False
            if not node:
                return False
            # If the value is equal to the node's value, return True
            if node.value == value:
                return True
            # if the search value is less than the current node's value, search left 
            # otherwise, search right
            return _search(node.left, value) if value < node.value else _search(node.right, value)
        # Start the recursive search
        return _search(self.root, value)

    def inorder_traversal(self):
        # helper function to perform inorder traversal
        def _inorder(node):
            if node is None:
                return []
            # inorder traversal: left -> root -> right
            return _inorder(node.left) + [node.value] + _inorder(node.right)
        # start the traversal from the root
        return _inorder(self.root)
    
    # Helper function to get the height of a node
    def _get_height(self, node):
        # if the node is None, return height as 0
        return node.height if node else 0

    # Helper function to get the balance factor of a node
    def _get_balance(self, node):
        # if the node is None, return balance factor as 0
        # if the node is not None, return the difference between the height of left and right subtrees
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    # Helper function for rotation left
    def _rotate_left(self, unbalanced_node):
        # we define new_root as the right child of unbalanced_node
        new_root = unbalanced_node.right
        # we define transfer_subtree as the left child of new_root
        transfer_subtree = new_root.left

        # we assign the left child of new_root to unbalanced_node
        new_root.left = unbalanced_node
        # we assign the right child of unbalanced_node to transfer_subtree
        unbalanced_node.right = transfer_subtree

        # update the heights of unbalanced_node and new_root
        unbalanced_node.height = 1 + max(self._get_height(unbalanced_node.left), self._get_height(unbalanced_node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))
        # return new_root 
        return new_root
    

    # Helper function for rotation right
    def _rotate_right(self, unbalanced_node):
        #  we define new_root as the left child of unbalanced_node
        new_root = unbalanced_node.left
        # we define transfer_subtree as the right child of new_root
        transfer_subtree = new_root.right

        # we assign the right child of new_root to unbalanced_node
        new_root.right = unbalanced_node
        # we assign the left child of unbalanced_node to transfer_subtree
        unbalanced_node.left = transfer_subtree

        # update the heights of unbalanced_node and new_root
        unbalanced_node.height = 1 + max(self._get_height(unbalanced_node.left), self._get_height(unbalanced_node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))
        # return new_root
        return new_root 