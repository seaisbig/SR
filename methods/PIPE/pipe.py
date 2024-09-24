import numpy as np
from gplearn.genetic import SymbolicRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

# 生成模拟数据
X = np.random.uniform(-1, 1, 100).reshape(-1, 1)
y = X**2 + X + 2 + np.random.normal(0, 0.1, X.shape)

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建一个包含数据预处理和符号回归的Pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),  # 预处理：标准化数据
    ('symbolic_regressor', SymbolicRegressor(population_size=5000, generations=20, 
                                             stopping_criteria=0.01, p_crossover=0.7, 
                                             p_subtree_mutation=0.1, p_hoist_mutation=0.05, 
                                             p_point_mutation=0.1, max_samples=0.9, 
                                             verbose=1, parsimony_coefficient=0.01, 
                                             random_state=42))
])

# 训练模型
pipe.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = pipe.predict(X_test)

# 计算均方误差
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# 输出最佳符号回归方程
best_program = pipe.named_steps['symbolic_regressor']._program
print(f"Best found program:\n{best_program}")
