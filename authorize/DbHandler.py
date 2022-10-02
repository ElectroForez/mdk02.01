from mysql.connector import connect, Error as MySqlError


class DbHandler:
    def __init__(self):
        self.connection = connect(
            host='localhost',
            user='admin',
            password='qwerty',
            database='demoTraining'
        )
        self.cursor = self.connection.cursor()
        print('База данных запущена')

    def get_user(self, login, password):
        self.cursor.execute(f'SELECT * FROM Workers WHERE '
                            f'Логин="{login}" '
                            f'AND '
                            f'Пароль="{password}"')
        result = self.cursor.fetchone()
        print(result)
        return result

# Пример пользователя из БД
# Ivanov@namecomp.ru
# 2L6KZG
