# Assignment – Operations on AVL Trees

## Comparative Analysis

### 1. How the structure & height change  
#### Leftist Tree  
- **Insertion** – You just *merge* the new single-node heap with the old one.  
  - After each merge, you may swap the two children so that the **null-path-length (npl)** rule holds (right child’s npl ≤ left child’s npl).  
  - Because of that rule, the *shortest* path is always on the right, so the tree “leans” left.  
  - Height stays about **O(log n)** on random data, but can hit **O(n)** if you’re super unlucky.  
- **Deletion (delete-min)** – Throw away the root, then just merge its two sub-heaps. Same npl swaps happen, so the height ends up like insertion.  
- **Merging** – This is the star move: two heaps are merged recursively, doing the npl swap trick on the way back up. Runs in **O(log n)** time.

#### Binary Heap  
- A complete binary tree kept in an array.  
- **Insert**: stick the new key at the end, bubble it up → height = ⌊log₂ n⌋.  
- **Delete-min**: move last item to root, bubble it down → height = log n.  
- **Merge**: ugly — you basically have to rebuild (≈ O(n)).

#### Unbalanced BST  
- **Insert/Delete** just follow the key order. No balancing ⇒ height can grow to **n**.  
- **Merge** two arbitrary BSTs? Usually flatten both to sorted arrays or do tricky rotations ⇒ **O(n)**.

#### AVL Tree  
- Always keeps balance factor -1, 0, +1.  
- **Insert/Delete** might trigger 1-2 rotations, guaranteeing height ≤ 1.44 log₂ n → **O(log n)**.  
- **Merge** (aka “join”) takes one tree, splits the other, then stitches → **O(m + log n)** where m = smaller tree size.

---

### 2. Efficiency side-by-side

| Operation          | Leftist Tree | Binary Heap |  Unbalanced BST | AVL Tree |
|--------------------|-------------:|------------:|----------------:|---------:|
| Insert             | **O(log n\*)** | O(log n)   | O(n)            | O(log n) |
| Delete-min/Delete  | **O(log n\*)** | O(log n)   | O(n)            | O(log n) |
| Merge              | **O(log n)**  | O(n)       | O(n)            | O(m + log n) |

\*expected; worst-case O(n) if the tree degenerates.

---

### 3. What really matters
- **Need lots of merges? → pick a Leftist Tree.** It’s literally built for that.
- **Want guaranteed height bounds? → AVL (or a Binary Heap if you don’t care about merge).**
- **Binary Heap** wins when you only do insert + delete-min and like the tight, cache-friendly array layout.
- **BST without balancing** is fine for tiny or already-sorted data, but can go downhill fast.

In short: **Leftist Trees trade perfect balance for super-fast melds**, making them great in algorithms (like external sorting or Huffman coding) that constantly combine heaps.
