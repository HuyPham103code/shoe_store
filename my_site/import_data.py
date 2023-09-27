import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import datetime


#read file
csv_file = r"D:\Năm 3\các công cụ lập trình hiện đại\my_site\data.csv"
df = pd.read_csv(csv_file)



#connect to database
try:
    connection = mysql.connector.connect(
        host="localhost",
        database="shoe_store",
        user="root",
        password="robinhoD1"
    )

    if connection.is_connected():
        cursor = connection.cursor()

        print('successfully!')
except Error as e:
    print("Error while connecting to MySQL:", e)



#import data
for record in df.to_records(index=False):
    category, img, title, price = record
    insert_query = f"""
    INSERT INTO shoe_shoe (category, img, title, price, created_date)
    VALUES ('{category}', '{img}', '{title}', '{price}', '{datetime.now()}')
    """

    cursor.execute(insert_query)
    connection.commit()


if connection.is_connected():
    cursor.close()
    connection.close()
