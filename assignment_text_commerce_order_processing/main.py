class Order:
    def __init__(self, order_id, customer_name, order_details):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_details = order_details

    def __str__(self):
        return f"OrderID: {self.order_id}, Customer: {self.customer_name}, Details: {self.order_details}"


class Node:
    def __init__(self, order):
        self.order = order
        self.next = None


class OrderLinkedList:
    def __init__(self):
        self.head = None

    def append(self, order):
        new_node = Node(order)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.order)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        self.display()