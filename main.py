import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np

from read_data import ReadData


"""Create ReadData objects"""

read_data = ReadData("CH4_Flux_BigTrail_Goldstream_AK.csv")

"""Run functions"""
read_data.return_data_file()
read_data.return_data_table()

data = ["work", wakacje, lep, klep, dsdssd, "sdsds"]
# return day temp info from api in json
