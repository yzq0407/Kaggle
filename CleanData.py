import numpy as np
import pandas as pd

train  = pd.read_csv('/Users/Theodore/Documents/Codes/Data/Kaggle/Datasets/train.csv', dtype = {'is_booking': bool})

aggs = []

print('-'*38)

for chunk in train:
  agg = chunk.groupby(['srch_destination_id', 'hotel_cluster'])['is_booking'].agg(['sum', 'count'])
  agg.reset_index(inplace = True)
  aggs.append(agg)
  print('. ')
print ('')
aggs = pd.concat(aggs, axis=0)
aggs.head()
