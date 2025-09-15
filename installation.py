# installation.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_prepare_data():

    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    df = pd.read_csv('cs_tickets.csv')

    df['request_date'] = pd.to_datetime(df['request_date'])
    
    print("Data loading and preprocessing complete")
    
    return df

if __name__ == "__main__":
    df = load_and_prepare_data()
    print("\n--- Data sample ---")
    print(df.head())
