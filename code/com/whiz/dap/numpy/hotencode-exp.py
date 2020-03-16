

import numpy as np;

data = np.array([3,1,0,1,7]);

print(data)

max_data = data.max();
len_of_data = len(data);
hotenc = np.zeros(shape=(len_of_data,max_data+1));
print(hotenc )
index = 0
for ele in data:
    print(ele)
    hotenc[index][ele] = True
    index = index+1

print(hotenc)
