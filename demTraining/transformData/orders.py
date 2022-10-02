import pandas as pd

dataFolder = '~/Documents/Study/МДК_02.01/training1/Сессия 1/'

df_orders = pd.read_excel(dataFolder + 'Заказы_import.xlsx')

df_orders['Дата закрытия'] = pd.to_datetime(df_orders['Дата закрытия'], format='%d/%m/%Y')
df_orders['Дата создания'] = pd.to_datetime(df_orders['Дата создания'], format='%d/%m/%Y')


def time_to_minutes(s: str):
    value, unit = s.split()
    value = int(value)
    if unit.startswith('мин'):
        value //= 60
    return value


df_orders['Время проката'] = df_orders['Время проката'].apply(time_to_minutes)

df_orders['Код заказа'] = df_orders['Код заказа'].apply(lambda x: x.split('/')[0])

new_orders_data = []
for row in df_orders.iterrows():
    row = row[1]
    id = row['ID']
    for service_id in row['Услуги'].split(', '):
        new_orders_data.append([id, service_id])

df_orders = df_orders.drop('Услуги', axis=1)

services = pd.DataFrame(new_orders_data, columns=['ID', 'Услуги'])
services.to_csv(dataFolder + 'transformData/services_orders.csv', index=False)

df_orders.to_csv(dataFolder + 'transformData/orders.csv', index=False)
