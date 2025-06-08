# Assignment – Operations on Binary Search Trees (BSTs)

## Discussion

- **Insertion**: As we insert values, the BST maintains its order property. Each value is placed to the left or right depending on its comparison with the current node.
- **Deletion**: 
  - Deleting a **leaf** is straightforward — just set it to `null`.
  - For a **node with one child**, we copy the child’s value to the node.
  - If a node has **two children**, we replace it with its inorder successor (smallest value in the right subtree).
- **Search**: The search for `12` follows the path: 15 → 10 → 12. This shows the BST allows efficient lookup using comparisons at each level.
