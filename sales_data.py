''' sales_data.py - Process a large CSV into individual customer Excel spreadsheets.
COMP 593 Scripting Applications Winter 2025 Lab 3.
Louis Bertrand <louis.bertrand@flemingcollege.ca>
'''

from sys import argv  # needed for command line parameter
from os import path  # Needed to check for file
import os  # Needed for makedirs
from datetime import date  # Needed for ISO date format

def main():
    sales_csv = get_sales_csv()
    orders_dir = create_orders_dir(sales_csv)
    process_sales_data(sales_csv, orders_dir)

# Get path of sales data CSV file from the command line
def get_sales_csv():
    if len(argv) < 2:    # Req-1, Req-2 Check whether provide parameter is valid path of file
        print("Please provide the path to the CSV file. Exiting...")
        exit(0)
    if not path.isfile(argv[1]):
        print("The path does not point to a file. Exiting...")
        exit(0)
    return argv[1]

# Create the directory to hold the individual order Excel sheets
def create_orders_dir(sales_csv):
    # Get directory in which sales data CSV file reside
    dirname = path.dirname(path.realpath(sales_csv))
    # Determine the name and path of the directory to hold the order data files
    isodate = date.today().isoformat()
    # Create the order directory if it does not already exist
    orders_dir = path.join(dirname, f"Orders_{isodate}")
    if not path.isdir(orders_dir):
        os.makedirs(orders_dir)
    return

# Split the sales data into individual orders and save to Excel sheets
def process_sales_data(sales_csv, orders_dir):
    # Import the sales data from the CSV file into a DataFrame
    # Insert a new "TOTAL PRICE" column into the DataFrame
    # Remove columns from the DataFrame that are not needed
    # Group the rows in the DataFrame by order ID
    # For each order ID:
        # Remove the "ORDER ID" column
        # Sort the items by item number
        # Append a "GRAND TOTAL" row
        # Determine the file name and full path of the Excel sheet
        # Export the data to an Excel sheet
        # TODO: Format the Excel sheet
    return

if __name__ == '__main__':
    main()