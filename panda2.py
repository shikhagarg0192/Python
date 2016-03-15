import pandas as pd
import numpy as np

data = pd.read_csv("Data_loan/train_u6lujuX.csv", index_col = "Loan_ID")

print data.loc[(data["Gender"]=="Female") & (data["Education"]== "Not Graduate")
         & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]

