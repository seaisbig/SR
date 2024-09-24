# 导入pandas库，用于处理数据框
import pandas as pd
import numpy as np
# 从pysr库中导入PySRRegressor类，进行符号回归
from pysr import PySRRegressor

# 创建一个数据框 'data'，包含两个特征 x1 和 x2，以及目标变量 y
# 其中 x1 是 [1, 2, 3, 4]，x2 是 [2, 3, 4, 5]，y 是 [3, 5, 7, 9]
# 该数据表示线性关系，y 大致等于 x1 和 x2 的加权和
data = pd.DataFrame({
    'x1': [1, 2, 3, 6,7,3,2],  # 第一列特征 x1
    'x2': [2, 3, 4, 5,3,2,1],  # 第二列特征 x2
    'y':  [3, 5, 7, 9,3,2,2]    # 目标变量 y
})

# 初始化 PySRRegressor 模型，用于符号回归
# 参数 niterations=1000 表示模型将执行 1000 次迭代
# binary_operators 参数指定了可以在模型中使用的二元运算符（加、减、乘、除）
# unary_operators 参数指定了可以使用的单一运算符（sin、cos、exp 等数学函数）
model = PySRRegressor(
    niterations=1000,  # 迭代次数，表示算法在符号回归过程中要进行多少次搜索
    binary_operators=["+", "-", "*", "/"],  # 二元运算符，加法、减法、乘法、除法
    unary_operators=["sin", "cos", "exp"]  # 单一运算符，正弦、余弦、指数函数
)

# 使用 data 中的特征 x1 和 x2 作为输入变量，y 作为目标变量进行模型训练
# model.fit 会对数据进行符号回归，寻找 x1 和 x2 与 y 之间的数学关系
x=np.linspace(0, 10, 100).reshape(-1,1)
y = np.sin(np.cos(x)) + np.random.randn(1)
# model.fit(data[['x1', 'x2']], data['y'])
model.fit(x,y)
# 打印训练好的模型，查看模型发现的最佳数学表达式
# 输出结果是模型对输入和输出关系的符号表示
equations = model.equations_

# 输出所有方程式
print(equations)

# 自动选择最优的表达式：损失值最小的
best_eq = equations.iloc[equations['loss'].idxmin()]

# 输出最优表达式
print("最适合的表达式：", best_eq['equation'])

