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
After, yesterday's session I have a better understanding of what the project needs and how the Semaphores work in Python. 
Looking at the example.py and the thread_demo.py was really useful and I should do that if I get stuck in this session. 

The hardest part of the project will likely be implementing threads without having any deadlock issues and keeping the order 
tellers still intact. 

## Plan for this session

I need to complete the base Semaphores and shared variables, then I need to implement the teller functionality
fully.
After teller functionality I need to work on completing the customer functionality for the project. 

Then final stage is to complete the main function before running and testing the code. 


## Session Progress

Created the bank_sim.py file and did all the necessary inputs for it.

I then implemented the resource protection Semaphores: 
I have a safe_semaphore with a limit of 2, manager_semaphore with a limit of 1, door_semaphore with a limit of 2

I then wrote the functions for bank state management where I:
    - Created the bank_open semaphore
    - Added logic to track tellers_ready_count
    - dded logic for bank opening and closing

I then wrote the teller-customer interaction semaphores:
    - Created arrays of semaphores for each teller
    - Implemented semaphores for signaling between tellers and customers
    - Added protection for shared data (transaction types and customer IDs)

Completed the teller interaction semaphores:
    - Implemented the announcement of readiness
    - Added logic for waiting for customers
    - Implemented transaction handling
    - Added manager permission requests for withdrawals
    - Implemented safe usage with proper semaphore protection
    - Added transaction completion and customer departure handling


## Need to do

Complete the customer thread function:
- Finish the line waiting logic
- Implement the teller selection process
- Complete the transaction communication with teller
I- mplement leaving the bank


Complete the main function:
- Create and start all teller and customer threads
- Implement proper waiting for threads to complete
- Handle bank closing correctly


Test the implementation with a small number of customers first

Debug any issues that arise during testing
Implement proper error handling for edge cases


# Apr 10th 2025 - 10:00 am

## Thoughts so far, Started the project
I've made some good progress so far, checked my code again to see if it is working right and it looks all good to me. I got the teller function
logic done and it's handling both deposit and withdrawl transactions appropriately making sure the manager intercations are safe and properly synced.

## Plan for this session

Need to focus on completing the customer thread function and the main function to get the simulation fully working.

Complete the customer thread function:
- Finish the line waiting logic
- Implement the teller selection process
- Complete the transaction communication with teller
I- mplement leaving the bank


Complete the main function:
- Create and start all teller and customer threads
- Implement proper waiting for threads to complete
- Handle bank closing correctly


Test the implementation with a small number of customers first

Debug any issues that arise during testing
Implement proper error handling for edge cases



## Session Progress

Completed the customer thread, it can:
- do entry through the door with semaphore handling
- Teller selection logic allows customers to select an available teller or wait
- have a full communcation sequence with the teller


I also finished up the main function so I can check how the program is working.
The main works kind of like this:
- It first creates and starts 3 teller threads
- It also starts 50 customer threads
- Waits for all customers to be served before moving forward
- if the bank closes it also tells them that, like the instructions specified
- and it makes sure all the tellers are exited properly too. 


## Need to do

- Testing the functionality. 




# Apr 10th 2025 - 1:00 pm

## Thoughts so far, Started the project

The main code of the project is complete, I just need to test the project and hope nothing breaks or it doesn't take too long. 

## Plan for this session

- Test my code and make sure it is working, both with small sample and full 50 sample.
- Complete the ReadMe file for running instructions
- Commit, push and turn in the project.

## Session Progress



## Need to do

- Turn in the project
