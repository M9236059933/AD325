# TextWise Solutions – Simple Text Editor with Undo Functionality

## Clarifying Questions

* What should happen if the user tries to delete or undo when the text is already empty?
* Is there a limit on the number of undo operations or text size?
* Should the undo feature only revert the last operation, or can we redo operations as well?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity*** 

**Add Operation: O(1)**
Append 1 symbol to string O(1).
Push 1 operation onto the stack O(1).

**Delete Operation: O(1)**
Removing 1 symbol from string O(1).
Push 1 operation onto the stack O(1).

**Undo Operation: O(1)**
Pop 1 operation from the stack O(1).
Modifying the string O(1).

***Space Complexity*** 

**Add Operation: O(1)**
We create only 1 operation with 1 symbol O(1).

**Delete Operation: O(1)**
We take 1 symbol and create only 1 operation with 1 symbol O(1).

**Undo Operation: O(1)**
We don't create anything O(1).

