import threading
import random
import time

# Resource protection semaphores
safe_semaphore = threading.Semaphore(2)  # Only 2 tellers can be in the safe at once
manager_semaphore = threading.Semaphore(1)  # Only 1 teller can interact with the manager
door_semaphore = threading.Semaphore(2)  # Only 2 customers can enter at a time

# Bank state semaphores
bank_open = threading.Semaphore(0)  # Bank is closed until all tellers are ready
tellers_ready_count = 0
tellers_ready_mutex = threading.Semaphore(1)  # Protect the count

# Customer tracking
customers_served = 0
customers_served_mutex = threading.Semaphore(1)  # Protect the count
bank_closed = False

# Teller-customer interaction
teller_available = [threading.Semaphore(1) for _ in range(3)]  # Init to 1 as all will be available
customer_at_teller = [threading.Semaphore(0) for _ in range(3)]  # Signal that customer is at teller
transaction_requested = [threading.Semaphore(0) for _ in range(3)]  # Signal that teller has asked for transaction
transaction_told = [threading.Semaphore(0) for _ in range(3)]  # Signal that customer has told the transaction
transaction_done = [threading.Semaphore(0) for _ in range(3)]  # Signal that transaction is complete
customer_left = [threading.Semaphore(0) for _ in range(3)]  # Signal that customer has left

# Shared data for transaction type (0 for deposit, 1 for withdrawal)
transaction_types = [None, None, None]
transaction_types_mutex = threading.Semaphore(1)  # Protect transaction types

# Shared data for customer IDs at each teller
customer_ids = [None, None, None]
customer_ids_mutex = threading.Semaphore(1)  # Protect customer IDs

# Line management
line_mutex = threading.Semaphore(1)  # Protect the line operations

def teller(id):
    global tellers_ready_count, bank_closed
    
    # Teller announces they're ready
    print(f"Teller {id} []: ready to serve")
    
    # Increment tellers ready count and open bank if all tellers are ready
    tellers_ready_mutex.acquire()
    tellers_ready_count += 1
    if tellers_ready_count == 3:
        bank_open.release()  # Open the bank
    tellers_ready_mutex.release()
    
    # Main service loop
    while not bank_closed:
        # Announce waiting for a customer
        print(f"Teller {id} []: waiting for a customer")
        
        # Wait for a customer to approach
        customer_at_teller[id].acquire()
        
        # Exit if bank is closed
        if bank_closed:
            break
        
        # Get customer ID
        customer_id = customer_ids[id]
        
        # Announce serving the customer
        print(f"Teller {id} [Customer {customer_id}]: serving a customer")
        
        # Ask for transaction
        print(f"Teller {id} [Customer {customer_id}]: asks for transaction")
        transaction_requested[id].release()
        
        # Wait for customer to tell transaction
        transaction_told[id].acquire()
        
        # Get transaction type
        transaction_type = transaction_types[id]
        transaction_name = "deposit" if transaction_type == 0 else "withdrawal"
        
        # Handle the transaction
        print(f"Teller {id} [Customer {customer_id}]: handling {transaction_name} transaction")
        
        # For withdrawal, get permission from manager
        if transaction_type == 1:  # Withdrawal
            print(f"Teller {id} [Customer {customer_id}]: going to the manager")
            manager_semaphore.acquire()
            print(f"Teller {id} [Customer {customer_id}]: getting manager's permission")
            
            # Sleep to simulate interaction with manager (5-30ms) like specified
            time.sleep(random.randint(5, 30) / 1000)
            
            print(f"Teller {id} [Customer {customer_id}]: got manager's permission")
            manager_semaphore.release()
        
        # Go to the safe
        print(f"Teller {id} [Customer {customer_id}]: going to safe")
        safe_semaphore.acquire()
        print(f"Teller {id} [Customer {customer_id}]: enter safe")
        
        # Sleep to simulate transaction in safe (10-50ms) like specified
        time.sleep(random.randint(10, 50) / 1000)
        
        # Leave the safe
        print(f"Teller {id} [Customer {customer_id}]: leaving safe")
        safe_semaphore.release()
        
        # Inform customer the transaction is done
        print(f"Teller {id} [Customer {customer_id}]: finishes {transaction_name} transaction.")
        
        # Reset transaction type
        transaction_types_mutex.acquire()
        transaction_types[id] = None
        transaction_types_mutex.release()
        
        # Wait for customer to leave
        print(f"Teller {id} [Customer {customer_id}]: wait for customer to leave.")
        transaction_done[id].release()
        
        # Wait for customer to leave
        customer_left[id].acquire()
        
        # Check if all customers are served
        customers_served_mutex.acquire()
        global customers_served
        customers_served += 1
        if customers_served == 50:
            bank_closed = True
        customers_served_mutex.release()
        
        # Reset customer ID
        customer_ids_mutex.acquire()
        customer_ids[id] = None
        customer_ids_mutex.release()
        
        # Make teller available again
        teller_available[id].release()
    
    # Announce leaving for the day
    print(f"Teller {id} []: leaving for the day")

# Customer function - only basic structure defined so far
def customer(id):
    # Decide transaction type (0 is for a deposit, 1 for a withdrawal)
    transaction_type = random.randint(0, 1)
    transaction_name = "deposit" if transaction_type == 0 else "withdrawal"
    print(f"Customer {id} []: wants to perform a {transaction_name} transaction")
    
    # Wait a random time before entering bank (0 to 100ms), give space
    time.sleep(random.randint(0, 100) / 1000)
    
    # Wait for bank to open
    bank_open.acquire()
    bank_open.release()  # Release so other customers can check too
    
    # Customer goes to the bank
    print(f"Customer {id} []: going to bank.")
    
    # Enter through the door (only 2 at a time)
    door_semaphore.acquire()
    print(f"Customer {id} []: entering bank.")
    door_semaphore.release()  # Release after entering
    
    # Get in line
    print(f"Customer {id} []: getting in line.")
    
    # Customer is selecting a teller
    print(f"Customer {id} []: selecting a teller.")
    
    # Try to find an open teller
    selected_teller = None
    
    line_mutex.acquire()
    for i in range(3):
        # Check if teller is actually available (non-blocking)
        if teller_available[i].acquire(blocking=False):
            selected_teller = i
            break
    line_mutex.release()
    
    # If no teller is there, wait until teller calls
    if selected_teller is None:
        # Wait until a teller becomes available
        while selected_teller is None and not bank_closed:
            for i in range(3):
                if teller_available[i].acquire(blocking=False):
                    selected_teller = i
                    break
            if selected_teller is None:
                # If no teller, sleep a bit to prevent busy waiting
                time.sleep(0.001)
    
    # If bank closed while waiting, just exit
    if bank_closed:
        return
        
    # Customer selects the teller
    print(f"Customer {id} [Teller {selected_teller}]: selects teller")
    
    # Set customer ID for the teller
    customer_ids_mutex.acquire()
    customer_ids[selected_teller] = id
    customer_ids_mutex.release()
    
    # Customer introduces itself
    print(f"Customer {id} [Teller {selected_teller}] introduces itself")
    
    # Signal teller that customer is at the counter
    customer_at_teller[selected_teller].release()
    
    # Wait for teller to ask for transaction
    transaction_requested[selected_teller].acquire()
    
    # Tell the teller the transaction type
    print(f"Customer {id} [Teller {selected_teller}]: asks for {transaction_name} transaction")
    
    # Set transaction type for the teller
    transaction_types_mutex.acquire()
    transaction_types[selected_teller] = transaction_type
    transaction_types_mutex.release()
    
    # Transaction has been started/told
    transaction_told[selected_teller].release()
    
    # Wait for transaction to finish up
    transaction_done[selected_teller].acquire()
    
    # Leave the teller
    print(f"Customer {id} [Teller {selected_teller}]: leaves teller")
    
    # Customer has left teller
    customer_left[selected_teller].release()
    
    # Leave the bank through the door
    print(f"Customer {id} []: goes to door")
    print(f"Customer {id} []: leaves the bank")


# Main function
def main():
    global bank_closed
    
    # Create the nneded teller threads
    teller_threads = []
    for i in range(3):
        t = threading.Thread(target=teller, args=(i,))
        teller_threads.append(t)
        t.start()
    
    # Create the needed customer threads
    customer_threads = []
    for i in range(50):
        c = threading.Thread(target=customer, args=(i,))
        customer_threads.append(c)
        c.start()
    
    # Wait for all customer threads to finish
    for c in customer_threads:
        c.join()
    
    # Flag that the bank is closed
    bank_closed = True
    
    # Let all tellers know just in case they're waiting for customers
    for i in range(3):
        customer_at_teller[i].release()
    
    # Wait for all teller threads to finish
    for t in teller_threads:
        t.join()
    
    print("The bank closes for the day.")

if __name__ == "__main__":
    main()