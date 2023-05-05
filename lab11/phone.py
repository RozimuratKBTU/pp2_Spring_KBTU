import psycopg2
from users_list import use_list
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")

text = input()
if text == '1':
    def search_records(pattern):

        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE name LIKE %s OR phone LIKE %s", (f"%{pattern}%", f"%{pattern}%"))
        records = cur.fetchall()
        cur.close()
        conn.close()
        return records

    # Example usage
    results = search_records("55")
    print(results)

if text == '2':
    def insert_user(name, phone):
        cur = conn.cursor()
        cur.execute("SELECT id FROM users WHERE name = %s", (name))
        result = cur.fetchone()
        if result is not None:
            cur.execute("UPDATE users SET phone = %s WHERE id = %s", (phone, result[0]))
        else:
            cur.execute("INSERT INTO users (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        cur.close()
        conn.close()
    results = insert_user('John Doe','123-456-7890')
    print(results)

if text == '3':
    def insert_users(use_list):

        cur = conn.cursor()
        bad_data = []
        for user in use_list:
            name, phone = user.split(',')
            if len(phone) != 10 or not phone.isdigit():
                bad_data.append(user)
            else:
                cur.execute("INSERT INTO users (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        cur.close()
        conn.close()
        if bad_data:
            return bad_data


    results = insert_users(use_list)
    print(results)


if text == '4':
    def get_users(limit, offset):

        cur = conn.cursor()
        cur.execute("SELECT id, name, phone FROM users ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
        records = cur.fetchall()
        cur.close()
        conn.close()
        return records

    results = get_users(1, 5)
    print(results)


