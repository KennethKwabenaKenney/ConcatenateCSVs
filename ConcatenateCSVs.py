# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:14:41 2024

@author: kenneyke
"""
import os
import pandas as pd

def combine_csv_files(input_folder):
    # Get input folder name
    folder_name = os.path.basename(input_folder)
    parent_folder = os.path.dirname(input_folder)
    output_file = f"{folder_name}.csv"

    # List all CSV files in the input folder
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the input folder.")
        return

    # Initialize an empty list to store DataFrames
    dfs = []

    # Combine data from each CSV file
    for csv_file in csv_files:
        file_path = os.path.join(input_folder, csv_file)
        df = pd.read_csv(file_path)
        dfs.append(df)

    # Concatenate all DataFrames in the list
    combined_df = pd.concat(dfs, ignore_index=True)

    # Save the combined data to a CSV file within the parent folder of the input folder
    output_path = os.path.join(parent_folder, output_file)
    combined_df.to_csv(output_path, index=False)

    print(f"Combined data saved to {output_path}")


input_folder = r'D:\ODOT_SPR866\My Label Data Work\New Manual Labelling\6_Analysis\1HWY_Segment-Segment'
combine_csv_files(input_folder)


