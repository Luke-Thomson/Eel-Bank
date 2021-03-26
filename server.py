import eel
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("EelBank").sheet1
eel.init("web")


@eel.expose
def add(data1, data2, data3, data4):
    balance_list = sheet.col_values(1)

    change_total = data1
    transaction_type = data2
    reason = data3
    date = data4

    if transaction_type == "deposit":
        balance = str(float(balance_list[-1]) + float(change_total))
    elif transaction_type == "withdraw":
        balance = str(float(balance_list[-1]) - float(change_total))
    else:
        balance = balance_list[-1]

    line = [balance, change_total, transaction_type, reason, date]

    sheet.append_row(line)

    return line


@eel.expose
def delete_row():
    data = sheet.get_all_records()
    sheet.delete_row(len(data) + 1)


@eel.expose
def my_func():
    data = sheet.get_all_records()
    row_list = sheet.row_values(len(data) + 1)
    row = "/".join(row_list)
    return row


@eel.expose
def new_function():
    values_list = sheet.col_values(1)
    balance = values_list.pop()
    return balance


eel.start("bulma.html", port=1112, size=(590, 846))
