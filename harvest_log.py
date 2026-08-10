
import pandas as pd 

from datetime import date 

DB_FILE_PATH = "./db/harvest_main_log_df.csv"
# DB_FILE_PATH = "./db/harvest_main_df.csv"

class Harvest_Log:

    def __init__(self, harvest_log): 
        self.harvest_log = harvest_log
        print(self.harvest_log)
        self.harvest_log_df = pd.read_csv(DB_FILE_PATH)
        # print(self.harvest_log_df.head()) 

    def upd_harvest_log(self): 

        self.harvest_log_df = self.harvest_log_df.loc[:, ~self.harvest_log_df.columns.str.contains('^Unnamed')]
        
        if "Total" not in self.harvest_log_df.columns: 
            self.harvest_log_df["Total"] = 0 
        

        self.harvest_log_df["Date"] = pd.to_datetime(self.harvest_log_df["Date"])

        full_dates = pd.date_range(start = self.harvest_log_df["Date"].iloc[-1] + pd.Timedelta(days = 1), end = date.today(), freq = "D")

        full_dates_df = pd.DataFrame({"Date" : full_dates})

        self.harvest_log_df = pd.concat([self.harvest_log_df, full_dates_df], ignore_index = True)
        self.harvest_log_df['Date'] = self.harvest_log_df['Date'].dt.strftime('%Y-%m-%d')

        
        
        for log_date, name, val in self.harvest_log:
            # print(name)1
            flag = True   
            if name not in set(self.harvest_log_df.columns): 
                flag = int(input(f"Should i add new column : {name} ??"))
                print(flag, name)
                if flag == 1: 
                    default_value = 0 
                    if name == "Fertiliser" : default_value = None 
                    
                    self.harvest_log_df[name] = default_value  
                    print(f"Added {name} column")
                else: flag = False 

            if flag: 
                
                curr_datetime  = pd.to_datetime(log_date) if log_date is not None else pd.to_datetime(date.today())
                start_datetime = pd.to_datetime(self.harvest_log_df.Date.iloc[0]) 
                end_datetime = pd.to_datetime(self.harvest_log_df.Date.iloc[-1]) 

                print(curr_datetime , start_datetime, end_datetime)

                if curr_datetime  >= start_datetime and curr_datetime <= end_datetime: 
                    curr_date = str(log_date if log_date is not None else date.today())
                    # print(curr_date)

                    self.harvest_log_df.loc[(self.harvest_log_df["Date"] == curr_date), name] = val 
                    if name != "Fertiliser": 
                        self.harvest_log_df.loc[(self.harvest_log_df.Date == curr_date), "Total"] += val 

        col_names = ["Date", "Total"] + [col for col in self.harvest_log_df.columns if col not in ["Date", "Total"]]
        self.harvest_log_df = self.harvest_log_df[col_names]

        self.save_df()
        # print(self.harvest_log_df.iloc[-1].Total)
        print(self.harvest_log_df.iloc[-1])



    def save_df(self): 
        self.harvest_log_df = self.harvest_log_df.fillna(0) 
        print(self.harvest_log_df) 
        self.harvest_log_df.to_csv(DB_FILE_PATH, mode = "w", index = False) 

    def del_col(self, col_names): 
        self.harvest_log_df = self.harvest_log_df.drop(columns = col_names)
        self.save_df() 

if __name__ == "__main__": 

    today_date = str(date.today())
    harvest_log = [
    # ['2026-07-07', 'Hibiscus_F', 1],
    # ['2026-07-07', 'Tulsi_Sabja_L', 5],  
    #     ['2026-07-08', 'Hibiscus_F', 1], 
    #     ['2026-07-08', 'Tulsi_Sabja_L', 5], 
    #     ['2026-07-09', 'Hibiscus_F', 1], 
    #     ['2026-07-09', 'Tulsi_Rama_L', 5], 
    #     ['2026-07-09', 'Tulsi_Sabja_L', 5], 
    #     ['2026-07-10', 'Hibiscus_F', 1], 
    #     ['2026-07-10', 'Tulsi_Rama_L', 1], 
    # [None, "Double_Tagar_F", 1],
    # [None, "Hibiscus_F", 1],
    #  [None, "Curry_L", 7],
    # ["2026-06-01", "Curry_L", 10],
    # [None, "Hibiscus_F", 3], 
    # [None, "Tulsi_Rama_L", 7], 
    # [None, "Tulsi_Krishna_L", 7], 
    # [None, "Tulsi_Sabja_L", 7], 
    # [None, "Tulsi_Kapoor_L", 5], 
    # [None, "Double_Tagar_F", 1]
    # [None, "Hibiscus_F", 3],
    # ["2026-07-15", "Hibiscus_F", 2], 
    # ["2026-07-16", "Lemon_Grass_L", 1], 
    # ["2026-07-16", "Tulsi_Sabja_L", 7]
    # [None, "Tulsi_Rama_L", 5], 
    # [None, "Tulsi_Sabja_L", 7],
    # [None, "Hibiscus_F", 1], 
    # [None, "Double_Tagar_F", 1], 
    # [None, "Tulsi_Krishna_L", 5], 
    # ["2026-07-24", "Curry_L", 10],
    # [None, "Tulsi_Kapoor_L", 15], 
    # [None, "Jui_L", 50], 
    # [None, "Kolkata_Pan_L", 2], 
    # [None, "Lemon_Grass_L", 4]
    # [None, "Nirgundi_L", 25], 
    # [None, "Parijatak_L", 1]
    # [None, "Double_Tagar_F", 1], 
    # [None, "Tulsi_Rama_L", 5],
    # ["2026-07-29", "Double_Tagar_F", 1], 
    # ["2026-07-29", "Tulsi_Rama_L", 5], 
    # ["2026-07-29", "Tulsi_Sabja_L", 5]
    # [None, "Tulsi_Krishna_L", 5], 
    # [None, "Hibiscus_F", 1]
    # [None, "Hibiscus_F", 3],
    # [None, "Curry_L", 10], 
    # [None, "Tulsi_Rama_L", 15],
    # ["2026-08-02", "Hibiscus_F", 3], 
    # ["2026-08-02", "Double_Tagar_F", 1], 
    # ["2026-08-02", "Tulsi_Sabja_L", 5], 
    # ["2026-08-01", "Tulsi_Rama_L", 5]
    # [None, "Kolkata_Pan_L", 2]
    # [None, "Mogra_F", 1]
    # ["2026-08-05", "Mogra_F", 1],
    # ["2026-08-05", "Hibiscus_F", 2],
    # ["2026-08-06", "Hibiscus_F", 2],
    # ["2026-08-06", "Mogra_F", 1],
    # ["2026-08-07", "Hibiscus_F", 1],
    # [None, "Double_Tagar_F", 2], 
    # [None, "Tulsi_Sabja_L", 7], 
    # [None, "Tulsi_Rama_L", 7]
    # [None, "Brahmi_L", 4], 
    # [None, "Sita_Ashoka_L", 5]
    # [None, "Brahmi_L", 3], 
    # [None, "Hibiscus_L", 30],
    # [None, "Double_Tagar_F", 2],
    # [None, "Tulsi_Sabja_L", 7], 
    # [None, "Tulsi_Krishna_L", 7]
    ]

    hl = Harvest_Log(harvest_log)
    hl.upd_harvest_log() 

    # hl.del_col(["Rama_Tulsi_F", "Rama_Tulsi_F2"])
    


    # harvest_log = [
    #     ['2026-04-25','Hibiscus_F', 3],
    #     ['2026-04-26','Hibiscus_F', 2],
    #     ['2026-04-27','Hibiscus_F', 3],
    #     ['2026-04-28','Hibiscus_F', 2],
    #     ['2026-04-29','Hibiscus_F', 1],
    #     ['2026-04-30','Hibiscus_F', 2],
    #     ['2026-05-01','Hibiscus_F', 1],
    #     ['2026-05-02','Hibiscus_F', 5],
    #     ['2026-05-03','Hibiscus_F', 2],
    #     ['2026-05-04','Hibiscus_F', 2],
    #     ['2026-05-05','Hibiscus_F', 4],
    #     ['2026-05-06','Hibiscus_F', 3],
    #     ['2026-05-07','Hibiscus_F', 4],
    #     ['2026-05-08','Hibiscus_F', 3],
    #     ['2026-05-10','Hibiscus_F', 4],
    #     ['2026-05-11','Hibiscus_F', 4],
    #     ['2026-05-12','Hibiscus_F', 3],
    #     ['2026-05-13','Hibiscus_F', 2],
    #     ['2026-05-14','Hibiscus_F', 4],
    #     ['2026-05-15','Hibiscus_F', 4],
    #     ['2026-05-17','Hibiscus_F', 4],
    #     ['2026-05-19','Hibiscus_F', 1],
    #     ['2026-05-20','Hibiscus_F', 1],
    #     ['2026-05-21','Hibiscus_F', 1],
    #     ['2026-05-22','Hibiscus_F', 2],
    #     ['2026-05-23','Hibiscus_F', 3],
    #     ['2026-05-24','Hibiscus_F', 1],
    #     ['2026-05-25','Hibiscus_F', 2],
    #     ['2026-05-26','Hibiscus_F', 1],
    #     ['2026-05-27','Hibiscus_F', 2],
    #     ['2026-05-28','Hibiscus_F', 2],
    #     ['2026-05-30','Hibiscus_F', 1],
    #     ['2026-06-02','Hibiscus_F', 1],
    #     ['2026-06-03','Hibiscus_F', 1],
    #     ['2026-06-08','Hibiscus_F', 1],
    #     ['2026-06-14','Hibiscus_F', 1],
    #     ['2026-06-16','Hibiscus_F', 1],
    #     ['2026-06-18','Hibiscus_F', 2],
    #     ['2026-06-23','Hibiscus_F', 1],
    #     ['2026-06-24','Hibiscus_F', 1],
    #     ['2026-06-25','Hibiscus_F', 2],
    #     ['2026-06-27','Hibiscus_F', 4],
    #     ['2026-06-28','Hibiscus_F', 1],
    #     ['2026-06-29','Hibiscus_F', 1],
    #     ['2026-06-30','Hibiscus_F', 1],
    #     ['2026-07-01','Hibiscus_F', 1],
    #     ['2026-07-02','Kolkata_Pan_L', 1],
    #     ['2026-07-02','Hibiscus_F', 1],
    #     ['2026-07-02','Mogai_Pan_L', 1],
    #     ['2026-07-01','Tulsi_Rama_L', 4],
    #     ['2026-06-28','Aloe_Vera_L', 1],
    #     ['2026-06-28','Tulsi_Sabja_L', 4],
    #     ['2026-06-28','Tulsi_Rama_L', 4],
    #     ['2026-06-24','Parijatak_L', 6],
    #     ['2026-06-24','Tulsi_Rama_L', 6],
    #     ['2026-06-24','Lemon_Grass_L', 2],
    #     ['2026-06-25','Lemon_Grass_L', 2],
    #     ['2026-05-07','Tulsi_Rama_L', 4],
    #     ['2026-05-07','Tulsi_Sabja_L', 4],
    #     ['2026-05-07','Tulsi_Kapoor_L', 4],
    #     ['2026-05-11','Tulsi_Kapoor_L', 4],
    #     ['2026-05-11','Tulsi_Krishna_L', 4],
    #     ['2026-05-11','Pudina_L', 30],
    #     ['2026-05-11','Brahmi_L', 1],
    #     ['2026-05-11','Aloe_Vera_L', 1],
    #     ['2026-05-14','Tulsi_Kapoor_L', 10],
    #     ['2026-05-14','Tulsi_Rama_L', 5],
    #     ['2026-05-14','Nirgundi_L', 12],
    #     ['2026-05-15','Tulsi_Krishna_L', 8],
    #     ['2026-05-16','Tulsi_Rama_L', 4],
    #     ['2026-05-17','Tulsi_Rama_L', 4],
    #     ['2026-05-17','Tulsi_Krishna_L', 4],
    #     ['2026-05-17','Pippali_L', 1],
    #     ['2026-05-17','Adulsa_L', 2],
    #     ['2026-05-17','Nirgundi_L', 5],
    #     ['2026-05-18','Tulsi_Sabja_L', 4],
    #     ['2026-05-19','Tulsi_Sabja_L', 4],
    #     ['2026-05-19','Tulsi_Krishna_L', 4],
    #     ['2026-05-19','Pippali_L', 1],
    #     ['2026-05-19','Nirgundi_L', 2],
    #     ['2026-05-19','Tulsi_Rama_L', 4],
    #     ['2026-05-19','Kolkata_Pan_L', 1],
    #     ['2026-05-21','Tulsi_Rama_L', 4],
    #     ['2026-05-21','Tulsi_Krishna_L', 4],
    #     ['2026-05-21','Pudina_L', 10],
    #     ['2026-05-22','Pudina_L', 5],
    #     ['2026-05-06','Mogra_F', 1],
    #     ['2026-05-07','Mogra_F', 1],
    #     ['2026-05-08','Mogra_F', 3],
    #     ['2026-05-09','Mogra_F', 6],
    #     ['2026-05-10','Mogra_F', 5],
    #     ['2026-05-11','Mogra_F', 5],
    #     ['2026-05-12','Mogra_F', 2],
    #     ['2026-05-14','Mogra_F', 1],
    #     ['2026-06-03','Mogra_F', 3],
    #     ['2026-06-04','Mogra_F', 2],
    #     ['2026-06-05','Mogra_F', 7],
    #     ['2026-06-06','Mogra_F', 3],
    #     ['2026-06-07','Mogra_F', 2],
    #     ['2026-06-08','Mogra_F', 3],
    #     ['2026-06-09','Mogra_F', 8],
    #     ['2026-06-11','Mogra_F', 1],
    #     ['2026-05-25','Tulsi_Rama_L', 5],
    #     ['2026-05-25','Tulsi_Kapoor_L', 5],
    #     ['2026-05-27','Tulsi_Rama_L', 5],
    #     ['2026-05-27','Tulsi_Sabja_L', 5],
    #     ['2026-05-28','Tulsi_Sabja_L', 7],
    #     ['2026-05-28','Tulsi_Rama_L', 6],
    #     ['2026-05-30','Tulsi_Rama_L', 8],
    #     ['2026-05-31','Tulsi_Rama_L', 5],
    #     ['2026-05-31','Tulsi_Sabja_F', 1],
    #     ['2026-06-01','Tulsi_Rama_L', 5],
    #     ['2026-06-02','Neem_L', 5],
    #     ['2026-06-02','Tulsi_Krishna_L', 5],
    #     ['2026-06-03','Tulsi_Sabja_F', 1],
    #     ['2026-06-03','Tulsi_Sabja_L', 5],
    #     ['2026-06-04','Tulsi_Rama_L', 7],
    #     ['2026-06-07','Tulsi_Rama_L', 4],
    #     ['2026-06-07','Tulsi_Sabja_L', 4],
    #     ['2026-06-12','Tulsi_Sabja_F', 1],
    #     ['2026-06-12','Tulsi_Rama_L', 4],
    #     ['2026-06-15','Tulsi_Rama_L', 4],
    #     ['2026-06-18','Tulsi_Sabja_L', 4],
    #     ['2026-06-18','Tulsi_Kapoor_L', 4],
    #     ["2026-07-03", "Mogra_F", 1], 
    #     ["2026-07-03", "Tulsi_Kapoor_L", 5], 
    #     ["2026-07-03", "Tulsi_Sabja_L", 5],
    #     ["2026-07-05", "Hibiscus_F", 5], 
    #     ["2026-07-05", "Mogra_F", 3], 
    #     ["2026-07-05", "Tulsi_Rama_L", 5], 
    #     ["2026-07-05", "Tulsi_Sabja_L", 5],
    #     ["2026-07-05", "Tulsi_Krishna_L", 10],
    #     ["2026-07-06", "Tulsi_sabja_L", 7],
    #     ["2026-04-25", "Fertiliser", "JeevanAmrutham"],
    #     ["2026-05-22", "Fertiliser", "Banana_Tonic"], 
    #     ["2026-05-27", "Fertiliser", "ButterMilk_Tonic"], 
    #     ["2026-06-10", "Fertiliser", "Banana_Tonic"],
    #     ["2026-05-01", "Fertiliser", "Vermicompost"], 
    #     ["2026-05-16", "Fertiliser", "Epsum_Salt_Foliage"],
    #     ["2026-05-23", "Fertiliser", "Epsum_Salt_Foliage"],
    #     ["2026-05-30", "Fertiliser", "Epsum_Salt_Foliage"],
        
    # ]
    


    

