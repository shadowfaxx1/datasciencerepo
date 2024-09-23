import openpyxl
data = [
    ["yes", "yes", None, "ETrade Online", None],
    [None, None, None, None, None],
    ["yes", "No", 22099, "ETrade Online", None],
    ["yes", "No", 24457, "ETrade Online", None],
    ["yes", "No", 22793, "ETrade Online", None],
    ["yes", "No", 21229, "ETrade Online", None],
    ["yes", "No", 23438, "ETrade Online", None],
    ["yes", "No", 18999, "ETrade Online", None],
    ["yes", "No", 17323, "ETrade Online", None],
    ["yes", "No", 14058, "ETrade Online", None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    ["yes", "No", 11418, "ETrade Online", None],
    ["yes", "No", 8787, "ETrade Online", None],
    ["yes", "No", 6227, "ETrade Online", None],
    ["yes", "No", 9041, "ETrade Online", None],
    ["yes", "No", 10451, "ETrade Online", None],
    ["yes", "No", 5699, "ETrade Online", None],
    ["yes", "No", 8954, "ETrade Online", None],
    ["yes", "No", 7870, "ETrade Online", None],
    [None, None, None, None, None],
    ["yes", "No", 9303, "ETrade Online", None],
    ["yes", "No", 7621, "ETrade Online", None],
    ["yes", "No", 7846, "ETrade Online", None],
    ["yes", "No", 5989, "ETrade Online", None],
    ["yes", "No", 6267, "ETrade Online", None],
    ["yes", "No", 6418, "ETrade Online", None],
    ["yes", "No", 6164, "ETrade Online", None],
    ["yes", "yes", None, "ETrade Online", None],
    ["yes", "yes", None, "ETrade Online", None],
    ["yes", "No", 4345, "ETrade Online", None],
    ["yes", "No", 6674, "ETrade Online", None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    ["yes", "No", 4933, "ETrade Online", None],
    ["yes", "No", 3814, "ETrade Online", None],
    ["yes", "No", 4703, "ETrade Online", None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    ["yes", "No", 4978, "ETrade Online", None],
    ["yes", "No", 4978, "ETrade Online", None],
    ["No", "No", 4700, "RS Lighting", "₹4,974.00"],
    [None, None, None, None, None],
    [None, None, None, None, None],
    ["yes", "No", 3791, "ETrade Online", None],
    ["yes", "No", 4729, "ETrade Online", None],
    ["yes", "No", 4729, "ETrade Online", None],
    ["yes", "No", 2099, "ETrade Online", None],
    [None, None, None, None, None],
    [None, None, None, None, None]
]


existing_file = r"C:\Users\kaifk\lpth\selenium\project\amazon\scraper\sampler.xlsx"
book = openpyxl.load_workbook(existing_file)
sheet = book['Sheet1']
# Determine the start row and column to write the data
start_row = 43
start_column = 9

for i, row_data in enumerate(data):
    for j, value in enumerate(row_data):
        sheet.cell(row=start_row + i, column=start_column + j, value=value)

book.save(existing_file)