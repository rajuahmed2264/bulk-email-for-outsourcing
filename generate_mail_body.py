import pandas as pd
import random

def generate_mail_body(receiver_det):
    file_path = 'mail_body_list.xlsx'

    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    mail_body_list = df.to_dict(orient='records')

    mail_body_index = random.randint(0, len(mail_body_list)-1)

    mail_body= mail_body_list[mail_body_index]['Mail_body']
    mail_title = mail_body_list[mail_body_index]['mail_subject']

    mail_body = mail_body.replace('[client_name]', receiver_det['full_name'])
    mail_body = mail_body.replace('[client_designation]', receiver_det['current_position'])
    mail_body = mail_body.replace('[client_company]', receiver_det['company_name'])
    mail_body = mail_body.replace('[client_company]', receiver_det['company_name'])

    return mail_body, mail_title
    