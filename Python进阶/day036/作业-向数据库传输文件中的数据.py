import pymysql

conn = pymysql.connect(host="127.0.0.1",user="root",password="77963333",database="day36")
cur = conn.cursor()
with open("file1.txt","r",encoding="utf-8") as f:
    for i in f:
        book_name, author, press, price, publish_date=i.split("|")
        sql = """insert into book values(%s,%s,%s,%s,%s)"""
        cur.execute(sql,(book_name, author, press, int(price), publish_date))
        conn.commit()