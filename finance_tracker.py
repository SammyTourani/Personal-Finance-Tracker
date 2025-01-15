import pandas as pd
from data_manager import load_data, save_data

class FinanceTracker:
    def __init__(self, data_file='data/finance_data.json'):
        """
        Initialize the FinanceTracker with a specified data file.
        Load existing data if the file exists.
        
        Parameters:
            data_file (str): Path to the JSON data file.
        """
        self.data_file = data_file
        self.data = load_data(self.data_file)

    def add_transaction(self, date, description, amount, category, transaction_type):
        """
        Add a new transaction to the finance tracker.
        
        Parameters:
            date (str): The date of the transaction (YYYY-MM-DD).
            description (str): Description of the transaction.
            amount (float): Amount of the transaction.
            category (str): Category of the transaction (e.g., Food, Rent).
            transaction_type (str): Type of transaction ('Income' or 'Expense').
        """
        new_transaction = {
            'Date': date,
            'Description': description,
            'Amount': amount,
            'Category': category,
            'Type': transaction_type
        }
        self.data = self.data.append(new_transaction, ignore_index=True)
        save_data(self.data_file, self.data)
        print(f"Added {transaction_type}: {description} of ${amount} on {date}.")

    def view_transactions(self):
        """
        Display all transactions in a tabular format.
        """
        if self.data.empty:
            print("No transactions available.")
        else:
            print(self.data)

    def export_to_csv(self):
        """
        Export financial data to a CSV file for external analysis.
        """
        csv_file = self.data_file.replace('.json', '.csv')
        self.data.to_csv(csv_file, index=False)
        print(f"Data exported to {csv_file}.")
