# This file contains the DataLoader class, which is used to load data
class DataLoader:
    def __init__(self, data, *adapter):
        self.data = data # List of tuples
        self.adapter = adapter # An instance of DBAdmin class
    
    def prepare(self):
        self.data
        preparing_data = []
        for row in self.data:
            row = [f"\'{value}\'" for value in row]
            row.append("CURRENT_TIMESTAMP")
            values = ", ".join(row)
            preparing_data.append(f"({values})")
        rows = ", ".join(preparing_data)
        self.prepared_values = f"VALUES {rows}"
    
    def load(self):
        self.prepare()
        self.query = f"INSERT INTO video_clips (clip_name, clip_extension, clip_duration, clip_location) {self.prepared_data}"  # noqa: E501
        #self.adapter.cursor.execute(query)
        #self.adapter.conn.commit()
