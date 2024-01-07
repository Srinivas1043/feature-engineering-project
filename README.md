# Excel Feature Engineering

This Python script performs feature engineering on an Excel file, specifically designed for a file named "Purchase_sales_listing.xlsx" with a specified sheet name. The script splits the data in the first column based on a hyphen ("-") and creates two new columns, storing customer names and vehicle numbers separately. The resulting dataframe is then exported to a new Excel file named "feature_engineered_sales_listing.xlsx."

## Prerequisites

Make sure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

## Usage

Install the required Python packages using the following command:

```
pip install pandas openpyxl
```
1. Clone the repository or download the script.
```
git clone https://github.com/your-username/your-repository.git
cd your-repository

```

2. Run the script

```
python script_name.py

```

The script will prompt you to enter the file location and name (with the correct case sensitivity) and the sheet name to be accessed. It will then perform feature engineering on the specified Excel file and save the result to a new file.

## Customization
Modify the user_filename and user_sheetname variables at the beginning of the script to specify the input file and sheet name.
## Contributing
If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request. Contributions are welcome!
