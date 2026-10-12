
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

        total = 0 
        
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

                # print(curr_datetime , start_datetime, end_datetime)

                if curr_datetime  >= start_datetime and curr_datetime <= end_datetime: 
                    curr_date = str(log_date if log_date is not None else date.today())
                    # print(curr_date)

                    self.harvest_log_df.loc[(self.harvest_log_df["Date"] == curr_date), name] = val 
                    total += val 
            
        self.harvest_log_df["Total"] = self.harvest_log_df[[col for col in self.harvest_log_df.columns if col not in ["Date", "Total", "Fertiliser"]]].sum(axis = 1)

        col_names = ["Date", "Total"] + [col for col in self.harvest_log_df.columns if col not in ["Date", "Total"]]
        self.harvest_log_df = self.harvest_log_df[col_names]

        self.save_df()
        # print(self.harvest_log_df.iloc[-1].Total)
        # print(self.harvest_log_df.iloc[-1])



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

    # [None, "Double_Tagar_F", 4]

    # [None, "Double_Tagar_F", 1], 
    # [None, "Hibiscus_F", 1],
    # [None, "Guggul_T", 1] 

    # [None, "Hibiscus_F", 0], 
    # [None, "Jui_F", 0], 
    

    # ["2026-10-10", "Double_Tagar_F", 4], 
    # ["2026-10-10", "Tulsi_Sabja_L", 15], 
    # ["2026-10-10", "Hibiscus_F", 1],

    # ["2026-10-11", "Double_Tagar_F", 4], 
    # ["2026-10-11", "Neem_L", 1], 
    


    # ["2026-10-12", "Double_Tagar_F", 1], 
    # ["2026-10-12", "Tulsi_Rama_A", 30]





    # ["2026-10-03", "Hibiscus_F", 1], 
    # ["2026-10-03", "Dhatura_F", 0], 
    # ["2026-10-03", "Double_Tagar_F", 2],
    # ["2026-10-03", "Tulsi_Sabja_L", 5], 
    # ["2026-10-03", "Tulsi_Rama_L", 5],  


    # ["2026-10-02", "Hibiscus_F", 1], 
    # ["2026-10-02", "Dhatura_F", 1], 
    # ["2026-10-02", "Double_Tagar_F", 4],
    # ["2026-10-02", "Tulsi_Sabja_L", 5], 
    # ["2026-10-02", "Tulsi_Rama_L", 5],  

    # [None, "Hibiscus_F", 0], 
    # [None, "Double_Tagar_F", 2], 
    # [None, "Tulsi_Sabja_L", 5], 
    # [None, "Insulin_L", 5], 
    # [None, "Aloe_Vera_L", 2], 


    # [None, "Double_Tagar_F", 3], 
    # [None, "Hibiscus_F", 1],
    # [None, "Tulsi_Rama_L", 5], 
    # [None, "Tulsi_Krishna_L", 5], 
    # [None, "Tulsi_Sabja_L", 7], 


    # ["2026-10-01", "Double_Tagar_F", 2],
    # ["2026-10-01", "Hibiscus_F", 2],
    # ["2026-10-01", "Tulsi_Rama_L", 5], 
    # ["2026-10-01", "Tulsi_Krishna_L", 5],
    # ["2026-10-01", "Dhatura_F", ] 
    # ["20206-10-01", "Tulsi_Sabja_L", 7], 

    # ["2026-09-24", "Double_Tagar_F", 6], 


    # [None, "Hibiscus_F", 2],
    # [None, "Jui_F", 1], 
    # [None, "Double_Tagar_F", 2], 
    # [None, "Tulsi_Krishna_L", 5], 
    # [None, "Tulsi_Sabja_L", 7], 


    # ["2026-09-26", "Hibiscus_F", 1], 
    # ["2026-09-26", "Jui_F", 1], 
    # ["2026-09-26", "Double_Tagar_F", 5], 
    # ["2026-09-26", "Tulsi_Rama_L", 7], 
    # ["2026-09-26", "Tulsi_Sabja_L", 7], 



    # ["2026-09-25", "Hibiscus_F", 5], 
    # ["2026-09-25", "Jui_F", 1], 
    # ["2026-09-25", "Double_Tagar_F", 2], 
    # ["2026-09-25", "Tulsi_Krishna_L", 5], 
    # ["2026-09-25", "Tulsi_Sabja_L", 7], 
    # ["2026-09-25", "Tulsi_Rama_L", 7], 
    # ["2026-09-25", "Tulsi_Kapoor_L", 5], 




    
    ]
    hl = Harvest_Log(harvest_log)
    hl.upd_harvest_log() 

    