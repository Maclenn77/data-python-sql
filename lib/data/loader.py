# This file contains the DataLoader class, which is used to load data
class DataLoader:
    def __init__(self, data):
        if type(data) != 'DataTransformer':
            raise TypeError("DataLoader class only accepts an instance of DataTransformer class")
        
        self.data = data
    
    