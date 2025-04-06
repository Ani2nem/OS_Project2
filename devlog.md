# Apr 6th 2025 - 11:00 am

## Thoughts so far, Started the project

So Project 2 needs me to simulate a bank with tellers and customers using threads and semaphores. After reading through the requirements, I know that I need to create a simulation with the following thingss:

- The bank has 3 tellers
- The bank opens only when all 3 tellers are ready
- 50 customers will visit the bank
- Customers perform either withdrawals or deposits (randomly determined)

Resource constraints:

- Only 2 tellers can be in the safe at once
- Only 1 teller can interact with the manager at a time
- Only 2 customers can enter through the door at a time


- Customers must wait in line if no teller is available
- The bank closes after all 50 customers have been served

This is essentially a thread synchronization problem with multiple shared resources and interaction patterns between different types of threads.


## Plan for this session

# Design the synchronization mechanisms - Identify all the semaphores and mutexes needed:

1. Resource protection semaphores (safe, manager, door)
2. Teller-customer interaction semaphores
3. Bank state semaphores (open/closed)
4. Line management structures


- Set up the basic code structure:

- Create the skeleton for teller and customer thread functions
- Implement the main function to create and start all threads
- Define all semaphores and shared variables


- Implement the teller thread function:

Logic for becoming ready
Waiting for customers
Asking for transaction details
Handling the transaction (manager approval for withdrawals)
Using the safe
Completing the transaction
Waiting for customer to leave


- Begin implementation of customer thread function:

Logic for transaction type selection
Waiting before entering bank
Entering through the door
Getting in line
Beginning of the teller interaction



I'll make sure to follow the proper output format for all actions and carefully test each component as I go. My goal is to have the basic structure and teller function implemented by the end of this session.

## Session Progress
Learned more about Semaphores and how they work in python, looked at HW 2 so I can get a better understading.
Worked on the structure for the code, the structure of how I want my program to run. 


## Need to do
Implement the learning and complete the testing of the project to see if it is working right. 




# Apr 7th 2025 - 10:00 am

## Thoughts so far, Started the project

## Plan for this session

# Design the synchronization mechanisms - Identify all the semaphores and mutexes needed:


## Session Progress



## Need to do




