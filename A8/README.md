# Data Cleaning Scripts

This repository contains two bash scripts for cleaning and processing the `AB_NYC_2019.csv` dataset.

## Overview

1. **First Script**:
   - Removes trailing spaces and newlines from the CSV file.
   - Identifies and handles missing values by either removing or replacing them with "NA".
   - Removes duplicate entries.
   - Identifies and handles outliers in the "Price" column based on the Interquartile Range (IQR).
   - Replaces high outliers in the "Price" column with the median value.

2. **Second Script**:
   - Works with a dataset located at `/home/dumpling/AB_NYC_2019.csv`.
   - Saves the cleaned and processed data to `cleaned_AB_NYC_2019.csv`.

## Usage

1. **Prepare the Dataset**: Place your `AB_NYC_2019.csv` file in the `/home/dumpling/` directory.
   
2. **Run the Script**:
   - Open a terminal and run the script by executing:
     ```bash
     bash data_cleaning.sh
     ```

3. **Check the Output**: The cleaned dataset will be saved as `cleaned_AB_NYC_2019.csv` in the `/home/dumpling/` directory.

## Notes
- The script automatically handles missing values, duplicates, and outliers.
- Modify the file paths in the script if your dataset is located in a different directory.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
