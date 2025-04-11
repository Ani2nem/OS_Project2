# OS_Project2

## Description
This project simulates a bank with 3 tellers and 50 customers using threads and semaphores for synchronization in Python. The bank opens when all tellers are ready, and customers perform either deposits or withdrawals.

## Files
- `bank_sim.py`: Main simulation program implementing the bank functionality
- `devlog.md`: Development log tracking the progress and thought process throughout the project
- `README.md`: Documentation for running and understanding the project

## How to Run
To run the simulation from the command line:
`python3 bank_sim.py` 

To save the complete output to a file for better review (recommended due to large amount of output): 
`python3 bank_sim.py > output.txt`


## Note to TA ##
- I had an issue with seeing the full output with the console method because of terminal buffer issues. 
- I have a mac and my python start command is python3, so you might want to change that to python if it's another machine. 


## Project Details
The simulation implements a bank with the following specifications:
- 3 tellers serve customers
- 50 customers visit the bank
- Bank opens only when all 3 tellers are ready
- Customers perform either deposits or withdrawals (randomly decided)
- Only 2 tellers can be in the safe at any time
- Only 1 teller can interact with the manager at a time (for withdrawals)
- Only 2 customers can enter through the door at a time
- The bank closes after all 50 customers have been served

## Implementation
This project uses Python's threading module and semaphores to manage synchronization between threads. Each teller and customer is implemented as a separate thread with proper synchronization to prevent race conditions and resource conflicts.