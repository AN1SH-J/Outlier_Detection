# ReadME file to contain all the details, assumptions and suggested improvements

import pandas as pd
import numpy as np
import os 

# Function to select 30 random consecutive data points
def data_selection(file_path):
    df = pd.read_csv(file_path, header=None)
    # Assigning column names explicitly
    df.columns = ['Stock-ID', 'Timestamp', 'Price']
    
    # Ensure the file has enough rows
    max_start = len(df) - 30
    if max_start <= 0:
        raise ValueError("File has insufficient data to identify outliers")
    
    # Selecting 30 consecutive rows starting from a random index
    start_index = np.random.randint(0, max_start)
    return df.iloc[start_index:start_index + 30]

# Function to find outliers
def find_outliers(data):
    mean_val = data['Price'].mean()
    std_val = data['Price'].std()
    outlier_rule = 2 * std_val
    data['Deviation'] = data['Price'] - mean_val
    data['% Deviation'] = (data['Deviation'] / mean_val) * 100
    outliers = data[abs(data['Deviation']) > outlier_rule]
    return outliers

# Main function to process files
def process_files(input_dir, output_dir, file_limit):
    files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
    for file in files[:file_limit]:
        try:
            data = data_selection(os.path.join(input_dir, file))
            outliers = find_outliers(data)
            outliers.to_csv(os.path.join(output_dir, f"outliers_{file}"), index=False)
            print(f"Processed {file}, outliers saved.")
        except Exception as e:
            print(f"Error processing {file}: {e}")

# Define input/output directories and run
if __name__ == "__main__":
    input_directory = "input_data"  # Folder with .csv files
    output_directory = "output_data"  # Folder for results
    os.makedirs(output_directory, exist_ok=True)  # Create output folder if missing
    process_files(input_directory, output_directory, 6)  # Process up to 2 files
