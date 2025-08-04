import pandas as pd

def load_and_clean_data(filepath):
    """Load and clean the raw transaction data"""
    df = pd.read_csv(filepath)
    
    # Convert items to list format
    df['items'] = df['items'].str.split(', ')
    
    # Remove empty orders
    df = df[df['items'].apply(len) > 0]
    
    return df