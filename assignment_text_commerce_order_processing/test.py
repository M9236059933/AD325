import unittest
from main import Order, OrderLinkedList

class TestOrderLinkedList(unittest.TestCase):
    def setUp(self):
        self.orders = OrderLinkedList()
        self.orders.append(Order(1, "Alice", "TV"))
        self.orders.append(Order(2, "Bob", "iPhone"))
        self.orders.append(Order(3, "Charlie", "MacBook"))

    def test_append_single_order(self):
        single = OrderLinkedList()
        single.append(Order(99, "Chris", "AirPods"))
        self.assertIsNotNone(single.head)
        self.assertEqual(single.head.order.order_id, 99)

    def test_reverse_order(self):
        print("---Testing reverse order---")
        self.orders.reverse()
        self.assertEqual(self.orders.head.order.order_id, 3)

    def test_reverse_empty_list(self):
        print("---Testing reverse empty list---")
        empty = OrderLinkedList()
        empty.reverse()
        self.assertIsNone(empty.head)

    def test_reverse_single_node(self):
        print("---Testing reverse single node---")
        single = OrderLinkedList()
        single.append(Order(42, "Sarah", "iPhone"))
        single.reverse()
        self.assertEqual(single.head.order.order_id, 42)

if __name__ == "__main__":
    unittest.main()