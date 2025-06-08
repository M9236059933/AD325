# Assignment – Operations on AVL Trees

## Discussion

- **Insertion**: AVL Tree maintains the Binary Search Tree property and keeps the tree balanced after every insertion.
After inserting a node, the tree checks the balance factor at each ancestor node (from the inserted node up to the root).
If the balance factor becomes greater than 1 or less than -1, a rotation (single or double) is performed to restore balance.
- **Deletion**: 
  - Deleting a **leaf** node works the same as in BST — set the node to `null`, and then check for balance from the parent upward.
  - Deleting a **node with one child** involves replacing the node with its child and rechecking balance.
  - For a **node with two children**, we replace the node with its inorder successor, delete the original successor, and then perform any required rebalancing from that point up.
- **Search**: Searching for a value (like 12) still follows the same path as in a regular BST — e.g., 15 → 10 → 12.
However, AVL trees tend to have smaller height, making the path shorter in practice and search faster than in an unbalanced BST.

## Efficiency Observation

By maintaining strict balance, AVL Trees ensure that all operations (insert, delete, search) stay within O(log n) time. This is especially important for large datasets, where an unbalanced BST could degrade to O(n) in the worst case.
