import pandas as pd

df=pd.read_json("../Data set/SalesTransactions.json",
                encoding='utf-8' ,dtype='unicode')
print(df)