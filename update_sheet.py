import openpyxl
def update_specific_cel(row_no):
    # Replace 'your_file.xlsx' with the path to your Excel file
    file_path = 'sender_creds.xlsx'

    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)

    # Select the worksheet you want to update
    worksheet = workbook['all_mail']  # Replace 'Sheet1' with the name of the worksheet

    # Define the cell you want to update
    cell = worksheet[f'G{row_no}']  # Replace 'A1' with the cell address you want to update

    # Update the cell value
    cell.value = "sent"

    # Save the workbook with the updated value
    workbook.save(file_path)

    # Close the workbook
    workbook.close()
