import pandas as pd


class ReadData:
    import pandas as pd

    def __init__(self, lake_methan_history):
        self.lake_methan_history = lake_methan_history

    def return_data_file(self):

        print(
            "Read file: ",
            self.lake_methan_history,
            "\n",
        )

    def return_data_table(self):
        data_info = pd.read_csv(self.lake_methan_history)
        print("\n", self.lake_methan_history, ": \n")
        print(data_info.head())

    def return_max_methane_value(self):
        data_info = pd.read_csv(self.lake_methan_history)
        print("\n", self.lake_methan_history, "methane max: \n")
        print(data_info["methane"].max())

    def return_min_methane_value(self):
        data_info = pd.read_csv(self.lake_methan_history)
        print("\n", self.lake_methan_history, "methane min: \n")
        print(data_info["methane"].min())
