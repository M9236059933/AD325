# TextWise Solutions – Student Record Management System Using TreeMap

## Clarifying Questions

* Should GPAs be validated (e.g., between 0.0 and 4.0)?
* Should we allow bulk import/export of students?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity:***

**add student: O(1)**
Adding to a dictionary and checking if a key exists both take O(1) average time.
**delete student: O(1)**
Removing a key from the dictionary is O(1) average time.
**update student gpa: O(1)**
Lookup and update operations on the dictionary are O(1).
**display all: O(k log k)**
Sorting the keys (student IDs) takes O(k log k), where k is the number of students. Printing takes O(k).
**display above gpa: O(k)**
Iterating through all student records takes O(k).

***Space Complexity: O(k).***
We store up to k student records in the dictionary. Each Student object holds its own small amount of data (ID, name, GPA), so total space grows linearly with the number of students.
