class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, GPA: {self.gpa}"


class StudentRecordManager:
    def __init__(self):
        self.records = {}

    def add_student(self, id, name, gpa):
        if id in self.records:
            return False
        self.records[id] = Student(id, name, gpa)
        return True

    def delete_student(self, id):
        return self.records.pop(id, None) is not None

    def update_gpa(self, id, new_gpa):
        student = self.records.get(id)
        if not student:
            return False
        student.set_gpa(new_gpa)
        return True

    def display_all(self):
        print("All Student Records:")
        for id in sorted(self.records):
            print(self.records[id])

    def display_above_gpa(self, min_gpa):
        print(f"Students with GPA > {min_gpa}:")
        for student in self.records.values():
            if student.gpa > min_gpa:
                print(student)


def main():
    manager = StudentRecordManager()

    # Add records
    manager.add_student(101, "Alice", 3.4)
    manager.add_student(102, "Bob", 2.9)
    manager.add_student(103, "Charlie", 3.7)
    manager.add_student(104, "Diana", 3.0)
    manager.add_student(105, "Evan", 3.9)

    manager.display_all()

    # Update GPA
    manager.update_gpa(102, 3.1)
    print("\nAfter GPA update:")
    manager.display_all()

    # Delete a record
    manager.delete_student(104)
    print("\nAfter deleting student 104:")
    manager.display_all()

    # Display students with GPA > 3.0
    print("\nStudents with GPA > 3.0:")
    manager.display_above_gpa(3.0)


if __name__ == "__main__":
    main()