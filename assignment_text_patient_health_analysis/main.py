class HealthNode:
    def __init__(self, metric):
        self.metric = metric
        self.next = None


def isHealthRecordSymmetric(head):
    # Step 1: Find the middle of the list using Slow/Fast
    slow = head
    fast = head
    stack = []

    while fast and fast.next:
        stack.append(slow.metric)
        slow = slow.next
        fast = fast.next.next

    # Step 2: We skip the middle element for the odd list
    if fast:
        slow = slow.next

    # Step 3: Compare the second half with the stack
    while slow:
        if stack.pop() != slow.metric:
            return False
        slow = slow.next

    return True