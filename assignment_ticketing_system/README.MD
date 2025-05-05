# TextWise Solutions – Ticketing System Simulation

## Clarifying Questions

* What should happen if we try to process an empty queue?
* Do we need to support priorities or just FIFO?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(n)*** We create a ticket O(1) and we append it in queue O(1). Finally complexity depends from length of array O(n).
***Space Complexity: O(n)*** We create object O(1), we store all such objects in queue, it means we need memory equal len of queue O(n).

