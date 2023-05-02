import psycopg2
import csv
from config import data

connection = psycopg2.connect(
    **data
)

current = connection.cursor()

insert = """INSERT INTO phonebook VALUES (%s,%s,%s) returning *;"""

update = """UPDATE phonebook SET phone_number = %s WHERE first_name = %s;"""

select = """SELECT * FROM phonebook"""

delete ="""DELETE FROM phonebook WHERE first_name = %s;"""

while True:
    command = input('insert,update,select,delete,exit\n ')

    if command == 'insert':
        n = int(input('If you wanna download with csv file write down 1, otherwise 2\n'))
        if n == 1:
            with open("phone.csv", 'r') as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    connection.cursor().execute(insert, row)
            connection.commit()

        if n == 2:
            name = input('Write name: ')
            surname = input('Write last name: ')
            phoneNumber = input('Write number: ')
            current.execute(insert, (name, surname, phoneNumber))
            connection.commit()

    if command == 'update':
        name = input('Write name: ')
        phone_number = input('Write number: ')
        current.execute(update, (phone_number, name))
        connection.commit()

    if command == 'select':
        current.execute(select)
        print(*current.fetchall(), sep='\n')
        connection.commit()

    if command == 'delete':
        name = input('Write name: ')
        current.execute(delete, [name])
        connection.commit()
    if command == 'exit':
        break

current.close()
connection.commit()
connection.close()








