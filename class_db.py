import sqlite3
class Database():
    def __init__(self , db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("""create table if not exists Contact
                         (id integer primary key , fname text , lname text, address text , phon text)
                         """)
        self.con.commit()
    def fetch(self):
        self.cur.execute('select * from Contact')
        rows = self.cur.fetchall()
        return rows
    def insert(self,fname , lname , address , phone):
        self.cur.execute('insert into Contact(id ,fname , lname , address , phon) values(NULL , ? , ? , ? ,?)' , (fname , lname , address , phone))
        self.con.commit()

    def remove(self , id):
        self.cur.execute('delete from Contact where id = ?' , (id,))
        self.con.commit()
    
    def update(self , id , fname , lname , address , phone):
        self.cur.execute("""update Contact set fname = ? , lname = ? , address = ? , phon = ? 
                         where id = ? """, (fname , lname , address , phone , id))
        self.con.commit() 


    


        