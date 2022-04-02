def migrate(cursor):
    cursor.execute('''CREATE TABLE form_values (structure text, status integer, id integer , hash text)''')
