class PatientNode:
    def __init__(self, ssn, name, age):
        self.ssn = ssn
        self.name = name
        self.age = age
        self.next = None

    def __str__(self):
        return f"SSN: {self.ssn}, Name: {self.name}, Age: {self.age}"


def merge_patient_lists(head1, head2):
    node = PatientNode(0, "", 0)
    tail = node

    while head1 and head2:
        if head1.ssn <= head2.ssn:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    # If one of the lists is not empty, append it to the merged list
    tail.next = head1 if head1 else head2

    return node.next