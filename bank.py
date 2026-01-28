def atm_simulation():
    # Initial account state
    balance = 1000.0
    pin = "1234"
    is_running = True

    print("--- Welcome to the Python Digital Bank ---")

    # Simple Security Check
    input_pin = input("Please enter your 4-digit PIN: ")

    if input_pin != pin:
        print("Incorrect PIN. Access Denied.")
        return

    while is_running:
        print("\nMain Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print(f"Current Balance: ${balance:,.2f}")

        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print(f"${amount:,.2f} deposited successfully.")
            else:
                print("Invalid amount.")

        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            if amount > balance:
                print("Insufficient funds!")
            elif amount <= 0:
                print("Invalid amount.")
            else:
                balance -= amount
                print(f"${amount:,.2f} withdrawn successfully.")

        elif choice == '4':
            print("Thank you for using our ATM. Have a great day!")
            is_running = False

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm_simulation()