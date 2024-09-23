from scraper2.scraper2 import amazon
import time 
import openpyxl
from prettytable import PrettyTable 
from bs4 import BeautifulSoup as bs
bot=amazon(headless=True)
try:
    with bot:
        data=bot.search_items()
        table = PrettyTable(
            field_names = ["title"]


        )
        table.add_rows(data)
        # Save the data to an Excel file using openpyxl
        print(table)
        existing_file = r"C:\Users\kaifk\lpth\.vscode\DataSciencePrac\practice\amazon.xlsx"

    
        book = openpyxl.load_workbook(existing_file)
        sheet = book['Sheet1']
        start_row = 1
        start_column = 2

        for i, row_data in enumerate(data):
            for j, value in enumerate(row_data):
                sheet.cell(row=start_row + i, column=start_column + j, value=value)

        book.save(existing_file)

except Exception as e:
    print("Error Occured hello : =",e)
    
time.sleep(100)


