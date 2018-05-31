import sqlite3


class TodoDB():
    def __init__(self):
        self.conn = sqlite3.connect("myDB.db")

    def cursor(self):
        return self.conn.cursor()

    def close(self):
        return self.conn.close()

    def commit(self):
        return self.conn.commit()

    def read_all(self):
        cursor = self.cursor()
        cursor = cursor.execute("select id,content from list")
        data = cursor.fetchall()
        cursor.close()
        # data = [d[0] for d in data]
        # print(data)
        return data

    def init_db(self):
        conn = sqlite3.connect('myDB.db')
        cursor = conn.cursor()
        cursor.execute(
            "create table list(id INTEGER PRIMARY KEY AUTOINCREMENT,content varchar(500),time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,title varchar(100))")
        cursor.execute(
            "create table user (id INTEGER PRIMARY KEY AUTOINCREMENT, username varchar(20), userpwd varchar(30))")
        cursor.close()
        conn.commit()
        conn.close()

    def delete_list(self, list_id):
        # 创立链接   获取游标
        cursor = self.cursor()
        cursor = cursor.execute("delete from list where id=?", (list_id,))
        cursor.close()
        self.commit()
        return

    def read(self, list_id):
        cursor = self.cursor()
        cursor = cursor.execute("select id,content from list where id=?", (list_id,))
        data = cursor.fetchone()
        print(data)
        cursor.close()
        return data


if __name__ == "__main__":
    db = TodoDB()
    # db.init_db()
    db.read(8)
