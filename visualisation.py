import matplotlib.pyplot as plt

def visualize_expenses(data):
    """
    Visualize expenses by category using a pie chart.
    
    Parameters:
        data (DataFrame): Financial data containing transactions.
    """
    if data[data['Type'] == 'Expense'].empty:
        print("No expenses to visualize.")
        return

    expense_data = data[data['Type'] == 'Expense']
    category_expenses = expense_data.groupby('Category')['Amount'].sum()

    plt.figure(figsize=(10, 6))
    category_expenses.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Expenses by Category')
    plt.ylabel('')
    plt.show()

def visualize_income_vs_expenses(data):
    """
    Visualize income versus expenses using a bar chart.

    Parameters:
        data (DataFrame): Financial data containing transactions.
    """
    if data.empty:
        print("No transactions to visualize.")
        return

    summary = data.groupby('Type')['Amount'].sum()
    summary.plot(kind='bar', color=['green', 'red'])
    plt.title('Income vs Expenses')
    plt.ylabel('Amount ($)')
    plt.xticks(rotation=0)
    plt.show()
