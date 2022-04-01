import sqlite3

connection = sqlite3.connect("hotel-system.sqlite")

cursor = connection.cursor()


def migrate():
    cursor.execute('''CREATE TABLE form_values (structure text, status integer, id integer , hash text)''')
