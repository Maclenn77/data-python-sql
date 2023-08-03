import sys
import os
required_paths = ['lib/data', 'lib/db', 'lib/adapter']
for path in required_paths:
    sys.path.append(path)
from admin import DBAdmin  # noqa: E402
from extractor import DataExtractor  # noqa: E402
from transformer import DataTransformer  # noqa: E402
from loader import DataLoader  # noqa: E402

# Create dir video_clips if doesn't exist
if not os.path.exists("video_clips"):
    os.makedirs("video_clips")
    print("Directory video_clips created")

# If videoclips directory is empty, request to add video clips
if not os.listdir("video_clips"):
    print("Please add video clips to video_clips directory and run again")
    sys.exit()

# Extract data from video clips
data_extractor = DataExtractor("video_clips")
data_extractor.extract()

# Transform data
transformer = DataTransformer(data_extractor)
transformer.transform()

# Prepare data
loader = DataLoader(transformer.transformed_data)
loader.prepare()

    
# Create an instance of DBAdmin
db_admin = DBAdmin()

# Connect to the database
db_admin.adapter.connect()

if not db_admin.adapter.is_connected():
    print("Database connection failed")
    sys.exit()
# Table name
table_name = "video_data"
# Create a list of columns
columns = [["clip_name", "VARCHAR(255)"],
           ["clip_file_extension", "VARCHAR(4)"],
           ["clip_duration", "INTERVAL"],
           ["clip_location", "VARCHAR(255)"],
           ["insert_timestamp", "TIMESTAMP"]
           ]

# Create a table video_data if not exists
db_admin.create_table(table_name, columns)

# Load data
db_admin.load_data(table_name, columns, loader.prepared_values)

db_admin.close()

