# Assignment – Operations on Binary Heaps


### Heap Property Analysis

- **Min-Heap** always ensures the **smallest element is at the root**.
- **Insertions** require *bubbling up* to restore the heap property if violated.
- **Deletions** (removal of root) require *bubbling down* to maintain the correct structure.
- The heap is always a **complete binary tree**, meaning it's completely filled on each level except possibly the last, and filled from left to right.

### Efficiency Discussion

- **Insertion**: `O(log n)` — bubbling up through the tree levels.
- **Deletion (root)**: `O(log n)` — bubbling down to correct position.
- **Search**: `O(n)` — not efficient, as there is no ordering between siblings or subtrees.

### Compare with other
- **AVL Tree**: Also `O(log n)` but requires **rotations** for balancing.
- **Binary Search Tree (BST)**: Can degrade to `O(n)` if not self-balanced.

Binary Heaps are highly efficient and ideal for **priority queue** use cases:

- Provide **guaranteed fast insertions and deletions**.
- Always maintain a **compact and predictable structure**.
- Easier to implement than **AVL Trees**, especially when self-balancing is not critical.
- **Not suitable for fast search or range queries** — lack of order makes searching inefficient (`O(n)`).
