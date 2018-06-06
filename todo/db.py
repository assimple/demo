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

    def init_db(self):
        conn = sqlite3.connect('myDB.db')
        cursor = conn.cursor()
        cursor.execute(
            "create table IF not EXISTS list(id INTEGER PRIMARY KEY AUTOINCREMENT,content varchar(500),time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,title varchar(100))")
        cursor.execute(
            "create table user (id INTEGER PRIMARY KEY AUTOINCREMENT, username varchar(20), userpwd varchar(30))")
        cursor.close()
        conn.commit()
        conn.close()

    def read_all(self):
        cursor = self.cursor()
        cursor = cursor.execute("select id,content,status from list order by id desc")
        data = cursor.fetchall()
        cursor.close()
        # data = [d[0] for d in data]
        # print(data)
        return data

    # 数据库迁移
    def migrate_latest(self):
        self.init_db()
        self.s2_add_status_column()

    def delete_list(self, list_id):
        # 创立链接   获取游标
        cursor = self.cursor()
        cursor = cursor.execute("delete from list where id=?", (list_id,))
        cursor.close()
        self.commit()

    def read(self, list_id):
        cursor = self.cursor()
        cursor = cursor.execute("select id,content,status from list where id=?", (list_id,))
        data = cursor.fetchone()
        print(data)
        cursor.close()
        return data

    def update_status(self, list_id, status):
        cursor = self.cursor()
        cursor = cursor.execute("update list set status = ? where id=?", (status, list_id))
        self.commit()
        data = cursor.fetchone()
        cursor.close()
        return data

    def create(self, text):
        cursor = self.cursor()
        cursor = cursor.execute("insert into list(content,status) values(?,\'doing\')", (text,))
        cursor.close()
        self.commit()

    def select_list(self, text):
        cursor = self.cursor()
        cursor = cursor.execute("select id from list where content=?", (text,))
        data = cursor.fetchone()
        print(data)
        cursor.close()
        return data

    # 修改表
    def s2_add_status_column(self):
        conn = sqlite3.connect('myDB.db')
        cursor = conn.cursor()
        cursor.execute("alter table list add column status varchar default 'done'")
        cursor.close()
        conn.commit()
        conn.close()


if __name__ == "__main__":
    db = TodoDB()
    # db.init_db()
    db.read(29)
    # db.select_list("test2")
    # db.migrate_latest()
    # db.update_status("done",30)
