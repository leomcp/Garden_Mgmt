import pandas as pd 
from datetime import date 

class Fertiliser_Log: 

    def __init__(self, fertiliser_log): 
        self.fertiliser_log = fertiliser_log 
        self.df = pd.read_csv("db/fertiliser_log.csv")

    def add_log_data(self): 

        for date, fertiliser in self.fertiliser_log: 
            curr_df = pd.DataFrame([{
                "Date" : date if date else date.today(), 
                "Fertiliser" : fertiliser 
            }])

            self.df = pd.concat([self.df, curr_df], ignore_index = False)
        self.df.Date = pd.to_datetime(self.df.Date)
        print(self.df)
        self.save_df()

    def save_df(self): 
        self.df = self.df.sort_values(by = ["Date", "Fertiliser"], ignore_index = True)
        self.df.to_csv("db/fertiliser_log.csv", index = False, mode = "w")
        print(f"Fertiliser_log.csv saved successfully !!!")




if __name__ == "__main__": 

    # fertliser_log = [
        # ["2026-04-23", "JeevanAmrutham"],
        # ["2026-05-22", "Banana_Tonic"], 
        # ["2026-05-27", "ButterMilk_Tonic"], 
        # ["2026-06-10", "Banana_Tonic"],
        # ["2026-05-01", "Vermicompost"], 
        # ["2026-05-16", "Epsum_Salt_Foliage"],
        # ["2026-05-23", "Epsum_Salt_Foliage"],
        # ["2026-05-30", "Epsum_Salt_Foliage"]
    # ]
    # ]

    fertiliser_log =[
        # ["2026-05-01", "Vermicompost"], 
        # ["2026-05-16", "Epsum_Salt_Foliage"],
        # ["2026-05-23", "Epsum_Salt_Foliage"],
        # ["2026-05-30", "Epsum_Salt_Foliage"] 
    ]

    fl = Fertiliser_Log(fertiliser_log) 
    fl.add_log_data()
    
