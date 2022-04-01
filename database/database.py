import sqlite3

connection = sqlite3.connect("hotel-system.sqlite")

cursor = connection.cursor()

cursor.execute("SELECT Count() FROM sqlite_master WHERE type='table' AND name='form_values'")

if cursor.fetchone()[0] < 1:
    import migration

    migration.migrate()

cursor.execute("INSERT INTO form_values VALUES('{}', 1, 1,'first-one')")

connection.commit()
