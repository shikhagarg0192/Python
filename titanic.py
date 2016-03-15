import pandas as pd
import sys
sys.stdout.flush()

df = pd.read_csv("Data/titanic/train.csv", header = 0)
print df.info()
print(sum(df['Cabin'].isnull()))
sum(df['Cabin'].isnull())

