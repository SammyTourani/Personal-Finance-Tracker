import os
import json
import pandas as pd

def load_data(data_file):
    """
    Load financial data from a JSON file.

    Parameters:
        data_file (str): Path to the JSON file.

    Returns:
        DataFrame: Loaded financial data or an empty DataFrame if no file exists.
    """
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return pd.DataFrame(json.load(f))
    
    return pd.DataFrame(columns=['Date', 'Description', 'Amount', 'Category', 'Type'])

def save_data(data_file, data):
    """
    Save financial data to a JSON file.

    Parameters:
        data_file (str): Path to the JSON file.
        data (DataFrame): Financial data to save.
    """
    with open(data_file, 'w') as f:
        json.dump(data.to_dict(orient='records'), f)
