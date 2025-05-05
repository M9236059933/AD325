import unittest
from main import Ticket, TicketQueue

class TestTicketQueue(unittest.TestCase):
    def test_ticket_creation(self):
        t = Ticket(1)
        self.assertEqual(t.number, 1)

    def test_generate_tickets(self):
        tq = TicketQueue()
        tq.generate_tickets(3)
        self.assertEqual(len(tq.queue), 3)

    def test_process_queue(self):
        tq = TicketQueue()
        tq.generate_tickets(3)
        self.assertEqual(len(tq.queue), 3)
        tq.process_tickets()
        self.assertEqual(len(tq.queue), 0)
        tq.generate_tickets(1)
        self.assertEqual(len(tq.queue), 1)
        tq.process_tickets()
        self.assertEqual(len(tq.queue), 0)
        tq.process_tickets()
        self.assertEqual(len(tq.queue), 0)