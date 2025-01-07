'''from numpy import nan as NA
##import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)
cleaned = data.dropna()
print(cleaned)
cleaned2=data.dropna(how='all')
print(cleaned2)'''

import pandas as pd
import numpy as np

# Tạo dữ liệu mẫu
data = pd.DataFrame([[1., 6.5, 3.],
                    [1., np.nan, np.nan],
                    [np.nan, np.nan, np.nan],
                    [np.nan, 6.5, 3.]])

# In dữ liệu gốc
print("Dữ liệu gốc:")
print(data)
print("\n" + "-"*40 + "\n")

''''# Cách 1: dropna() - loại bỏ tất cả hàng có ít nhất một NA
print("1. Loại bỏ tất cả hàng có ít nhất một NA:")
cleaned1 = data.dropna()
print(cleaned1)
print("\n" + "-"*40 + "\n")

# Cách 2: dropna(how='all') - loại bỏ hàng có tất cả giá trị là NA
print("2. Loại bỏ hàng có tất cả giá trị là NA:")
cleaned2 = data.dropna(how='all')
print(cleaned2)
print("\n" + "-"*40 + "\n")

# Cách 3: dropna(thresh=n) - giữ lại hàng có ít nhất n giá trị không phải NA
print("3. Giữ lại hàng có ít nhất 2 giá trị không phải NA:")
cleaned3 = data.dropna(thresh=2)
print(cleaned3)
print("\n" + "-"*40 + "\n")'''

# Cách 4: dropna(subset=[]) - chỉ xét NA trên một số cột
print("4. Chỉ xét NA trên cột 0 và 1:")
cleaned4 = data.dropna(subset=[0, 1])
print(cleaned4)