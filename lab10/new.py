import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

cur = con.cursor()
#
with cur as cursor:
    cursor.execute(
        """CREATE TABLE snake(
        name_ varchar(50) NOT NULL,
        total_score int);"""
    )
    con.commit()
    print("[INFO] Table created succesfully")