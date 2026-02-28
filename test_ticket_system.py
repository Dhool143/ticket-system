 
import unittest
from ticket_system import TicketSystem
 
 
class TestTicketSystem(unittest.TestCase):
    
    
    
    # Normal teset 
    
    
    def test_generate_ticket(self):
        system = TicketSystem()
        system.generate_ticket()
        self.assertEqual(system.queue_size(), 1)
        
    def test_process_ticket(self):
        system = TicketSystem()
        system.generate_ticket()
        system.process_ticket()
        self.assertEqual(system.queue_size(), 0)
        
    def test_fifo_order(self):
        system = TicketSystem()
        system.generate_ticket()
        system.generate_ticket()
        first = system.process_ticket()
        self.assertEqual(first.number, 1)
        
        
        # edeg test
        
        
    def test_process_empty_of_queue(self):
        system = TicketSystem()
        result = system.process_ticket()
        self.assertIsNone(result)
        
        
    def test_large_number_of_tickets(self):
        system = TicketSystem()
        for _ in range (1000):
            system.generate_ticket()
        self.assertEqual(system.queue_size(), 1000)
            
            
    def test_multiple_process(self):
        system = TicketSystem()
        for _ in range(3):
            system.generate_ticket()
        for _ in range(3):
            system.process_ticket()
        self.assertEqual(system.queue_size(), 0)
            
            
            
if __name__ == "__main__":
    unittest.main()
    
        