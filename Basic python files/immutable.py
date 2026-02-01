import pandas as pd

series=pd.Series([1,2,3,4])
changed_series=series.drop(0)
print(series) #still 1 will exist immutable
print(changed_series)