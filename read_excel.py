import pandas as pd
from update_sheet import update_specific_cel
from get_receiver_details import get_receiver_details
from generate_mail_body import generate_mail_body
from mail_sender import send_mail
from clear_status import clear_sheet_colum
# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'sender_creds.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

sender_list = df.to_dict(orient='records')
df = []
for index, sender in enumerate(sender_list):
    sender_p = sender['app_password']
    status = sender["Status"]
    sender_mail = sender['Email']

    if isinstance(sender_p, str) and  isinstance(status, str) ==False:
        receiver_det = get_receiver_details()
        email_body, mail_title = generate_mail_body(receiver_det)
        sent_success = send_mail(sender_mail, sender_p, receiver_det, email_body, mail_title)
        index_spec = index + 2
        update_specific_cel(index_spec)
        with open('last_receiver_mail.txt', "w") as file:
            file.truncate(0)
        with open('last_receiver_mail.txt', "w") as file:
            file.write(receiver_det['email1'])

clear_sheet_colum()
