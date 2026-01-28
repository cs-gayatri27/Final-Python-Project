#**Simple ATM Simulation**
A lightweight Command Line Interface (CLI) application built in Python that mimics the core functionalities of a real-world ATM. This project focuses on logic flow, state management, and user input validation.

##**Features**
1. **Secure Access:** Basic PIN authentication to enter the system.
2. **Balance Inquiry:** Check your current account balance in real-time.
3. **Deposits & Withdrawals:** Update your balance instantly with input validation (prevents overdrawing or invalid amounts).
4. **Currency Formatting:** Uses Python f-strings (:.2f) to ensure all financial data displays with proper decimal precision.
5. **Session Management:** A continuous loop allows for multiple transactions until the user chooses to exit.

##**Tech Stack**
1. **Language:** Python 
2. **Concepts used:** Loops (while), Conditional Logic (if/elif/else), Variable State, and String Formatting.

##**What I Learned**
1. Through this project, I practiced:
2. Managing user state in a running application.
3. Handling edge cases (e.g., preventing negative deposits).
4. Formatting floats for a better User Experience (UX).

##**Future Improvements**
1. Add a Transaction History log.
2. Integrate a File System (CSV or JSON) to save the balance after closing the program.
3. Implement Multiple User Accounts using dictionaries.
