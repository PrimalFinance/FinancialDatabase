from DataManager.data_manager import DataManager

import os
import shutil

source = "D:\\Coding\\VisualStudioCode\\Projects\\Python\\AssetCompare\\Storage"
destination = "D:\\FinancialData\\Database\\EquityData\\Stocks"


def move():
    # Loop through each file in the source directory
    for stock_folder in os.listdir(os.path.join(source, "QuarterData")):
        # Create the new directory structure
        new_stock_path = os.path.join(destination, stock_folder)
        statements_path = os.path.join(new_stock_path, "Statements")
        quarter_path = os.path.join(statements_path, "Quarter")
        annual_path = os.path.join(statements_path, "Annual")

        # Create directories if they don't exist
        os.makedirs(quarter_path, exist_ok=True)
        os.makedirs(annual_path, exist_ok=True)

        # Move annual data
        source_annual = os.path.join(source, "AnnualData", stock_folder)
        destination_annual = os.path.join(annual_path, stock_folder)
        shutil.move(source_annual, annual_path)


if __name__ == "__main__":
    move()
    # ticker = "AAPL"
    # dm = DataManager()

    # ticker_list = dm.get_ticker_list()

    # for t in ticker_list:
    #     dm.get_earnings(t)
