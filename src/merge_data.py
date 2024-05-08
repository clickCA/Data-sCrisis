import os
import glob
import pandas as pd

# Path to the directory containing the CSV files
data_dir = '../data/{year}/'

# Get a list of all the years
years = [str(year) for year in range(2018, 2025)]  # Replace with your desired range

# Iterate over each year
for year in years:
    # Create the output directory if it doesn't exist
    output_dir = f'../merge/'
    os.makedirs(output_dir, exist_ok=True)

    # Get a list of all the CSV files for the current year
    csv_files = glob.glob(os.path.join(data_dir.format(year=year), '*.csv'))
    print(csv_files)

    # Merge the CSV files into a single DataFrame
    merged_df = pd.concat([pd.read_csv(file) for file in csv_files])
    # Merge the CSV files into a single DataFrame

    # Set column 'eid' as index
    merged_df.set_index('sid', inplace=True)
    # Save the merged DataFrame to a CSV file
    output_file = os.path.join(output_dir, f'{year}.csv')
    merged_df.to_csv(output_file, index=True)
    # output_file = os.path.join(output_dir, f'{year}.feather')
    # merged_df.to_feather(output_file)  

    print(f'Merged {len(csv_files)} CSV files for {year} into {output_file}')