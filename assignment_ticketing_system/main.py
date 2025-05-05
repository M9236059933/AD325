from datetime import datetime
from collections import deque
import time
import random

class Ticket():
    def __init__(self, number):
        self.number = number
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Ticket #{self.number} - Time: {self.timestamp.strftime('%H:%M:%S')}"
    
class TicketQueue():
    def __init__(self):
        self.queue = deque()
        self.ticket_number = 1

    def generate_tickets(self, count):
        for _ in range(count):
            ticket = Ticket(self.ticket_number)
            self.queue.append(ticket)
            self.ticket_number += 1
            time.sleep(random.uniform(0.1, 0.5))  # random arrival time

    def process_tickets(self):
        while self.queue:
            ticket = self.queue.popleft()
            print(f"Serving: {ticket}")
            time.sleep(random.uniform(0.2, 0.7))  # random service time