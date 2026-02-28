#  Ticket Tracking System

##  Overview

This project implements a Ticket Tracking System for a service center using a Queue data structure. The system ensures that customers are served in the exact order they arrive, following the FIFO (First In, First Out) principle.

The implementation includes:
- Ticket generation with timestamp
- Queue-based ticket processing
- Simulation with random timing
- Unit tests (normal and edge cases)
- Time and space complexity analysis

---

##  Problem Statement

Customers take a ticket number and wait to be served. The system must:

1. Generate tickets with a unique number and timestamp.
2. Add tickets to a queue.
3. Process tickets in FIFO order.
4. Handle edge cases such as empty queues.
5. Simulate real-time ticket generation and processing.

---

##  System Design

The system consists of:

### 1️ Ticket Class
Stores:
- `ticket_number`
- `timestamp`

### 2️ TicketSystem Class
Maintains:
- A queue (`deque`)
- A ticket counter (`next_number`)

Provides:
- `generate_ticket()`
- `process_ticket()`
- `queue_size()`

---

##  Flow Diagram

Customer Arrives
↓
Create Ticket (number, timestamp)
↓
Enqueue into Queue
↓

Queue (FIFO)

Front → [T1] [T2] [T3] ← Rear

Process Ticket
↓
Dequeue from Front
↓
Serve Customer


## Code

You now have:

✔ Code  
✔ Tests  
✔ Diagram  
✔ Pseudocode  
✔ Complexity  
✔ Professional README  

---

If you'd like, I can also give you:

- A short LinkedIn-style project description  
- A GitHub commit message template  
- A 2-minute confident presentation script  

Tell me what you want next.