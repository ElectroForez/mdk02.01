import pandas as pd

dataFolder = '~/Documents/Study/МДК_02.01/training1/Сессия 1/'

df_clients = pd.read_excel(dataFolder + 'Клиенты_import.xlsx')

df_clients['Дата рождения'] = pd.to_datetime(df_clients['Дата рождения'], format='%d/%m/%Y')
df_clients['Серия паспорта'] = df_clients['Паспортные данные'].apply(lambda x: x.split()[1])
df_clients['Номер паспорта'] = df_clients['Паспортные данные'].apply(lambda x: x.split()[3])
df_clients.drop('Паспортные данные', axis=1, inplace=True)

df_clients.to_csv(dataFolder + 'transformData/clients.csv', index=False)