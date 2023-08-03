import psycopg2
import config

# Get environment variables
config = { "host": config.DB_HOST, 
          "database": config.DB_NAME,
          "user": config.DB_USER,
          "password": config.DB_PASSWORD,
          "port": config.DB_PORT 
          }

# Create an Postgres Adapter class
class Adapter:
    def __init__(self):
        self.config = config
        self.conn = None

    def connect(self):
        try:
          self.conn = psycopg2.connect(self.config)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        

    def disconnect(self):
        self.conn.close()
        self.conn = None
    
    def is_connected(self):
        return self.conn != None
    
    def cursor(self):
        if self.conn == None:
            self.connect()
        self.cursor = self.conn.cursor()

    def close_cursor(self):
        self.cursor.close()
        self.cursor = None
    
    def commit(self):
        self.conn.commit()