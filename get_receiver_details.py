import pandas as pd
from update_sheet import update_specific_cel
# Replace 'your_file.xlsx' with the path to your Excel file

def get_receiver_details():
    file_path = 'leads.xlsx'
    last_receiver = ''
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    with open('last_receiver_mail.txt', 'r') as file:
        last_receiver = file.read()

    receiver_list = df.to_dict(orient='records')
    df = []
    resume_selected = False
    receiver_info_ret = None 
    for receiver_info in receiver_list:
        if resume_selected:
            receiver_info_ret = receiver_info
            break
        if receiver_info['email1']== last_receiver:
            resume_selected = True
        if last_receiver=='':
            receiver_info_ret = receiver_info
            break
    return receiver_info_ret

