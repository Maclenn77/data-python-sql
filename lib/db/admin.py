from adapter import Adapter

class DBAdmin:
    def __init__(self):
        self.adapter = Adapter()
        self.adapter.connect()

    def query_excute(self, query):
        if self.adapter.is_connected():
            self.adapter.cursor.execute(query)
            self.adapter.conn.commit()
        else:
            print("Database connection failed")
            self.adapter.connect()
            self.adapter.cursor.execute(query)
    
    def create_table(self, table_name, columns):
        columns = [column[0] + " " + column[1] for column in columns]
        sql_columns = "(" + ", ".join(columns) + ")"
        query = "CREATE TABLE IF NOT EXISTS " + table_name + sql_columns
        print(query)
        self.query_excute(query)
        

    def get_data(self, table_name):
        query = "SELECT * FROM " + table_name
        self.adapter.cursor.execute(query)
        return self.adapter.cursor.fetchall()
            
    
    def drop_table(self, table_name):
        query = "DROP TABLE IF EXISTS " + table_name
        self.adapter.cursor.execute(query)
        self.adapter.conn.commit()


    def load_data(self, table_name, columns, values):
        columns = [column[0] for column in columns]
        sql_columns = "(" + ", ".join(columns) + ")"
        query = "INSERT INTO " + table_name + sql_columns + " " + values
        print(query)
        self.adapter.cursor.execute(query)
        self.adapter.conn.commit()

    
    def close(self):
        self.adapter.close_cursor()
        self.adapter.disconnect()
