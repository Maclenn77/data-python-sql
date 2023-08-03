from extractor import DataExtractor
from datetime import timedelta

# This file contains the DataTransformer class, which is used to transform data
class DataTransformer:
    def __init__(self, data):
        if isinstance(data, DataExtractor) is False:
            raise TypeError("DataTransformer class only accepts an instance of DataExtractor class")  # noqa: E501
        
        self.data = data # An instance of data extractor

    def transform(self):
        self.transformed_data = []
        for i in range(self.data.data_size):
            # Convert duration to time delta seconds and microseconds
            time = str(timedelta(seconds=self.data.video_clips_duration[i]))
            path = self.data.location + self.data.video_clips_files[i]

            # Create a tuple of data
            data = (self.data.video_clips_name[i],
                    self.data.video_clips_extension[i],
                    time, path)
            
            self.transformed_data.append(data)