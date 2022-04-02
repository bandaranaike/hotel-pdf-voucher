import database.seeders.form_seeder as form_seeder


def run(cursor, connection):
    form_seeder.run(cursor, connection)


print("seeder ran")
