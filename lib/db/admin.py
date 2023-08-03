from adapter import Adapter

class DBAdmin:
    def __init__(self):
        self.adapter = Adapter()
        self.adapter.connect()
        self.adapter.open_cursor()
    
    def create_table(self, table_name, columns):
        columns = [column[0] + " " + column[1] for column in columns]
        sql_columns = "(" + ", ".join(columns) + ")"
        query = "CREATE TABLE IF NOT EXISTS " + table_name + sql_columns
        self.adapter.cursor.execute(query)
        self.adapter.conn.commit()
    
    def drop_table(self, table_name):
        query = "DROP TABLE IF EXISTS " + table_name
        self.adapter.cursor.execute(query)
        self.adapter.conn.commit()


    def insert(self, table_name, columns, values):
        raise NotImplementedError
    
    def close(self):
        self.adapter.close_cursor()
        self.adapter.disconnect()
