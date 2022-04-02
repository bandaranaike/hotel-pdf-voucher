import sqlite3


def make_connection():
    connection = sqlite3.connect("C:\\Users\\User\\PycharmProjects\\pythonProject\\database\\hotel-system.sqlite")

    cursor = connection.cursor()

    cursor.execute("SELECT Count() FROM sqlite_master WHERE type='table' AND name='form_values'")

    # print(cursor.fetchone()[0])

    if cursor.fetchone()[0] == 0:
        print("DDD")
        import database.migration as migration
        import database.seeder as seeder

        migration.migrate(cursor)
        seeder.run(cursor, connection)

    return connection, cursor


print("database connector ran")
