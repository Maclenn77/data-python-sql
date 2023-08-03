import sys
import os
sys.path.append('lib/db')   # Add db_admin to path
sys.path.append('lib/adapter')   # Add adapter to path
from admin import Admin

# Create dir video_clips if doesn't exist
if not os.path.exists("../video_clips"):
    os.makedirs("../video_clips")

# If videoclips directory is empty, request add video clips
if not os.listdir("../video_clips"):
    print("Please add video clips to video_clips directory")
    sys.exit()
    
# Create an instance of Admin
db_admin = Admin()

# Connect to the database
db_admin.connect()

# Create a list of columns
columns = [["clip_name", "VARCHAR(255)"],
           ["clip_file_extension", "VARCHAR(3)"],
           ["clip_duration", "INTERVAL"],
           ["clip_location", "VARCHAR(255)"]]

# Create a table video_data
db_admin.create_table("video_data", columns)

