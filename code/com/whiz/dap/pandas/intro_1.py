import datetime as dt

import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta

df = pd.DataFrame({"name": ["a","b","c","d"], "age": [10, 20, 30, 40]})
ages = pd.Series([20, 30, 40], name="age", dtype=int)

data_series_size = 200
index = []
start_date = dt.datetime(2010, 1, 1)
for x in range(0, data_series_size):
    later = start_date + relativedelta(months=x)
    index.append(later.strftime("%d/%m/%Y"))

# ages_np_series  = pd.Series(np.array( [10,20,30,40,35]), name="age" , index=index)
ages_r_np_series = pd.Series(np.random.randint(20, 50, size=data_series_size), name="age", index=index)



ages_from_df = pd.Series(df.age)