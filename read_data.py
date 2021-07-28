import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np

class ReadData():
    import pandas as pd

    def __init__(self, lake_methan_history):
        self.lake_methan_history  = lake_methan_history

    def return_data_file(self):
        print("You read: ", self.lake_methan_history, "\n")
        

    def return_data_table(self):
        data_info = pd.read_csv(self.lake_methan_history)
        print(data_info)
        return data_info