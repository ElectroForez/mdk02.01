import pandas as pd

dataFolder = '~/Documents/Study/МДК_02.01/training1/Сессия 1/'

df = pd.read_excel(dataFolder + 'Сотрудники_import/Сотрудники_import.xlsx')

df['Последний вход'] = pd.to_datetime(df['Последний вход'], format='%d:%m:%Y %H:%M:%S')

df.to_csv(dataFolder + 'transformData/employers.csv', index=False)