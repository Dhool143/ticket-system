import time
import random
from collections import deque
from datetime import datetime



class Ticket:
    
    
    def __init__(self, number):
        self.number = number
        self.timestamp = datetime.now()
        
class TicketSystem:
    
    def __init__(self):
        self.queue = deque()
        self.next_number = 1
        
        
    def generate_ticket(self):
        ticket = Ticket (self.next_number)
        self.queue.append(ticket)
        self.next_number +=1
        
        
    def process_ticket(self):
        if not self.queue:
            return  None
        return self.queue.popleft()
    
    def queue_size(self):
        return len(self.queue)
    
    
    
def simulate():

    system = TicketSystem()

    print("/n--- Generate Ticket---")
    for _ in range(5):
        system.generate_ticket()
        print(f"Generate Ticket {system.next_number - 1}")
        time.sleep(random.uniform(0.5, 1.0))
    print("/n--- Process Tictes---")
    while system.queue:
        ticket = system.process_ticket()
        print(f"Serving Ticket {ticket.number}")
        time.sleep(random.uniform(0.5, 1.0))
        
        
        
if __name__ == "__main__":
    simulate()
        
    