import sqlite3


class TodoDB():
    def read_all(self):
        conn = sqlite3.connect("myDB.db")
        cursor = conn.cursor()
        cursor = cursor.execute("select id,content from list")
        data = cursor.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        # data = [d[0] for d in data]
        print(data)
        return data

    def init_db(self):
        conn = sqlite3.connect('myDB.db')
        cursor = conn.cursor()
        cursor.execute("create table list(id INTEGER PRIMARY KEY AUTOINCREMENT,content varchar(500),time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,title varchar(100))")
        cursor.execute("create table user (id INTEGER PRIMARY KEY AUTOINCREMENT, username varchar(20), userpwd varchar(30))")
        cursor.close()
        conn.commit()
        conn.close()

    def delete_list(self,list_id):
        print("delete；",list_id)


if __name__ == "__main__":
    db = TodoDB()
    # db.init_db()
    db.read_all()