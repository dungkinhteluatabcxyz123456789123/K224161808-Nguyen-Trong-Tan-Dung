'''from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)
cleaned=data.fillna(data.mean())
print(cleaned)'''

import pandas as pd
import numpy as np

# Tạo dữ liệu mẫu
data = pd.DataFrame([[1., 6.5, 3.],
                    [1., np.nan, np.nan],
                    [np.nan, np.nan, np.nan],
                    [np.nan, 6.5, 3.]])

print("Dữ liệu gốc:")
print(data)
print("-"*40)

# Cách 1: Điền bằng giá trị trung bình của cột
print("\n1. Điền bằng giá trị trung bình:")
cleaned1 = data.fillna(data.mean())
print(cleaned1)
print("-"*40)

# Cách 2: Điền bằng giá trị trước đó (forward fill)
print("\n2. Điền bằng giá trị trước đó:")
cleaned2 = data.fillna(method='ffill')
print(cleaned2)
print("-"*40)

# Cách 3: Điền bằng giá trị sau đó (backward fill)
print("\n3. Điền bằng giá trị sau đó:")
cleaned3 = data.fillna(method='bfill')
print(cleaned3)
print("-"*40)

# Cách 4: Điền các giá trị khác nhau cho từng cột
print("\n4. Điền giá trị cụ thể cho từng cột:")
values = {0: 0, 1: data[1].median(), 2: data[2].mode()[0]}
cleaned4 = data.fillna(value=values)
print(cleaned4)

