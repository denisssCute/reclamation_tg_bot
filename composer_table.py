import gspread

gc = gspread.service_account(filename='reclamation-project-70ca1b2a52cb.json')

sh = gc.open("Рекламации")
worksheet = sh.get_worksheet(0)
def get_clients():
    data = worksheet.col_values(1)
    clients = []

    for i in range(2, len(data), 1):
        if not(data[i] == ''):
            clients.append(data[i])
    return clients

def get_info(client):

    number_str_client = worksheet.find(client).row
    diapazon = f"A{number_str_client}:U{number_str_client}"

    titles = worksheet.row_values(2)
    data_client = []
    # data_client = worksheet.row_values(number_str_client)

    values_client = worksheet.range(diapazon)

    for cell in values_client:
        data_client.append(cell.value)



    data = titles, data_client

    return data

# print(get_info("dfghdf"))
print("Работаем!")
