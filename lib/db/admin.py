import sys
from adapter import Adapter

class Admin:
    def __init__(self):
        self.adapter = Adapter()
        self.adapter.connect()
        if not self.adapter.is_connected():
            print("Database connection failed")
            sys.exit()
        self.adapter.cursor()
    
    def create_table(self, table_name, columns):
        columns = [column[0] + " " + column[1] for column in columns]
        query = "CREATE TABLE IF NOT EXISTS " + table_name + "(" + {", ".join(columns)} + ")"
        self.adapter.cursor.execute(query)
        self.adapter.commit()
        self.adapter.close_cursor()
