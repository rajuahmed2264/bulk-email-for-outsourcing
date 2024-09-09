import openpyxl

def clear_sheet_colum():

    # Load your Excel file
    file_path = "sender_creds.xlsx"  # Replace with the path to your Excel file
    sheet_name = "all_mail"  # Replace with the name of the sheet you want to clear

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    # Specify the column you want to clear (e.g., column "A")
    column_to_clear = "G"

    # Convert the column label to a numeric column index
    column_index = openpyxl.utils.column_index_from_string(column_to_clear)

    # Loop through the rows and clear the specified column (skip the header)
    for row in sheet.iter_rows(min_row=2, min_col=column_index, max_col=column_index):
        for cell in row:
            cell.value = None

    # Save the modified workbook
    workbook.save(file_path)


clear_sheet_colum()