import sys
import os
required_paths = ['lib/data', 'lib/db', 'lib/adapter']
for path in required_paths:
    sys.path.append(path)
from admin import DBAdmin

# Create dir video_clips if doesn't exist
if not os.path.exists("video_clips"):
    os.makedirs("video_clips")
    print("Directory video_clips created")

# If videoclips directory is empty, request to add video clips
if not os.listdir("video_clips"):
    print("Please add video clips to video_clips directory and run again")
    sys.exit()

    
# Create an instance of DBAdmin
db_admin = DBAdmin()

# Connect to the database
db_admin.adapter.connect()

if not db_admin.adapter.is_connected():
    print("Database connection failed")
    sys.exit()

# Create a list of columns
columns = [["clip_name", "VARCHAR(255)"],
           ["clip_file_extension", "VARCHAR(4)"],
           ["clip_duration", "INTERVAL"],
           ["clip_location", "VARCHAR(255)"]]

# Create a table video_data if not exists
db_admin.create_table("video_data", columns)

