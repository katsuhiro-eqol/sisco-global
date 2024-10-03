import sqlite3
import csv

conn = sqlite3.connect('exams.db')

def create_table():
    cur = conn.cursor()
    #vector1: text-embedding-3-small, vecctor2: GiNZA
    #数値ベクトルを文字列に変換して保存する
    cur.execute('CREATE TABLE exams_list(id INTEGER PRIMARY KEY AUTOINCREMENT,body STRING, vector1 STRING, vector2 STRING)')
    conn.commit()

    conn.close()

def insert_body():
    cur = conn.cursor()
    with open("exams.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0])
            #cur.execute('INSERT INTO exams_list(name) values("Taro")')


insert_body()
