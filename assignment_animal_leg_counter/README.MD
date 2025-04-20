# Animal Leg Counter – Coding Interview Solution

## Clarifying Questions

* What if the animal name is not in the list?
* Can animals repeat in the list?
* Is letter case important?

## List of Animals and Their Leg Counts:

* Animals with Four Legs: 'lion', 'deer', 'elephant', 'horse', 'dog', 'cat'
* Animals with Two Legs: 'monkey', 'parrot', 'ostrich'
* Animals with No Legs: 'snake', 'worm'
* Animals with Multiple Legs (more than four): 'spider', 'ant', 'centipede'

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(n).*** We loop through the list once. The comparison operation is O(1). So complexity is O(n), where n is the length of the input animals array.

***Space Complexity: O(1).*** We  use one set to store the list of four-legged animals and one counter variable. So the memory we use stays the same no matter how many animals are in the list.