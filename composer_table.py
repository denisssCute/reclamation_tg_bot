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
    # return data

print(get_clients())
# get_clients()


# values_list = worksheet.row_values(1)

def get_info(client):
    data = get_clients().index(client)
    return data
