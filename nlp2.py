import pandas as pd
import BeautifulSoup as bs
train = pd.read_csv("Data/labeledTrainData.tsv", header=0, delimiter = "\t", quoting = 3)

print train.shape
print train.columns.values
eg1 =BeautifulSoup(train["review"][0])
print train["review"][0]
print eg1.get_text()
