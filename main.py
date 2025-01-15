from finance_tracker import FinanceTracker
from visualization import visualize_expenses, visualize_income_vs_expenses

def main():
    tracker = FinanceTracker()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Visualize Expenses")
        print("4. Visualize Income vs Expenses")
        print("5. Export Data to CSV")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            transaction_type = input("Enter transaction type (Income/Expense): ")
            tracker.add_transaction(date, description, amount, category, transaction_type)

        elif choice == '2':
            tracker.view_transactions()

        elif choice == '3':
            visualize_expenses(tracker.data)

        elif choice == '4':
            visualize_income_vs_expenses(tracker.data)

        elif choice == '5':
            tracker.export_to_csv()
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
