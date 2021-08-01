import pandas as pd


class ReadData:
    import pandas as pd

    def __init__(self, lake_methan_history, data_out):
        self.lake_methan_history = lake_methan_history
        self.data_out = data_out

    def return_data_file(self):

        print(
            "\n////// *** //////",
            "\nRead file: ",
            self.lake_methan_history,
            "\n",
        )

    def return_data_table(self):

        self.data_out = pd.read_csv(self.lake_methan_history)
        print("\n////// *** //////", "\n", self.lake_methan_history, ": \n")
        print(self.data_out.head())

    def return_max_methane_value(self):

        data_info = pd.read_csv(self.lake_methan_history)
        print("\n////// *** //////", "\n", self.lake_methan_history, "methane max: \n")
        self.data_out = data_info[["date", "methane"]].max()
        print(self.data_out)

    def return_min_methane_value(self):

        data_info = pd.read_csv(self.lake_methan_history)
        print("\n////// *** //////", "\n", self.lake_methan_history, "methane min: \n")
        self.data_out = data_info[["date", "methane"]].min()
        print(self.data_out)

    def return_describe_table(self):

        self.data_out = pd.read_csv(self.lake_methan_history)
        print("\n////// *** //////", "\n", self.lake_methan_history, "methane min: \n")
        print(self.data_out.describe())
