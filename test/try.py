import pandas as pd

data = pd.DataFrame({
    'x1': [1, 2, 3, 4],  # 第一列特征 x1
    'x2': [2, 3, 4, 5],  # 第二列特征 x2
    'y': [3, 5, 7, 9]    # 目标变量 y
})

print(data[['x1','x2']])