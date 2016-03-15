import pandas as pd
import numpy as np


#reading files
train = pd.read_csv("bigmart/Train.csv")
test = pd.read_csv("bigmart/Test.csv")

#gonna combine these so as to perform feature engg

#create 1 more column in each dataset to later separate them
train['source'] = 'train'
test['source'] = 'test'

data = pd.concat([train,test], ignore_index=True)
print train.shape, test.shape, data.shape

#check for missing values
print data.apply(lambda x: sum(x.isnull()))

print data.describe()

#filter categorical vars
catgrcl_cols = [x for x in data.dtypes.index if data.dtypes[x]=='object']
catgrcl_cols = [x for x in catgrcl_cols if x not in
                ['Item_Identifier','Outlet_Identifier','source']
