import pandas as pd 

from datetime import date 


if __name__ == "__main__":

    columns = ["Date"]

    df = pd.DataFrame(columns = columns)
    full_date = pd.date_range(start = "2026-04-25", end = date.today(), freq = "D")

    df["Date"] = full_date 

    df.to_csv("harvest_main_log.csv", index = False, mode = "w")



