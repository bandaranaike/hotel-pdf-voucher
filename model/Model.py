from database.database_connector import make_connection


class Model:
    def __init__(self, table):
        self.table = table
        self.connection, self.cursor = make_connection()

    def all(self):
        return self.cursor.execute(f"SELECT * FROM {self.table}")

    def get(self, column, value):
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE {column} = '{value}'")
        return self.cursor.fetchone()


print("Model ran")
