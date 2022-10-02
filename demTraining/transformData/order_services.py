import pandas as pd

dataFolder = '~/Documents/Study/МДК_02.01/training1/Сессия 1/'

df_orders = pd.read_excel(dataFolder + 'Заказы_import.xlsx')

new_orders_data = []
for row in df_orders.iterrows():
    row = row[1]
    id = row['ID']
    for service_id in row['Услуги'].split(', '):
        new_orders_data.append([id, service_id])

services = pd.DataFrame(new_orders_data, columns=['ID', 'Услуги'])
services.to_csv(dataFolder + 'transformData/order_services.csv', index=False)
