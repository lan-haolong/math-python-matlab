import numpy as np
import pandas as pd

A = pd.read_excel(r"E:\C.xlsx", usecols='E:H')

# 请输入初始矩阵[[55, 24, 10], [65, 38, 22], [75, 40, 18], [100, 50, 20]]


# 求出每一列的均值以供后续的数据预处理
Mean = np.mean(A, axis=0)

# 预处理后的矩阵
A_norm = A / Mean

print('预处理后的矩阵为：')
print(A_norm)

# 母序列
Y = A_norm.iloc[:, 0]

# 子序列
X = A_norm.iloc[:, 1:]

# 计算|X0-Xi|矩阵(在这里我们把X0定义为了Y)
absX0_Xi = np.abs(X.reset_index(drop=True).to_numpy() - np.tile(Y.reset_index(drop=True).to_numpy().reshape(-1, 1), (1, X.shape[1])))

# 计算两级最小差a
a = np.min(absX0_Xi)

# 计算两级最大差b
b = np.max(absX0_Xi)

# 分辨系数取0.5
rho = 0.5

# 计算子序列中各个指标与母序列的关联系数
gamma = (a + rho * b) / (absX0_Xi + rho * b)

print('子序列中各个指标的灰色关联度分别为：')
print(np.mean(gamma, axis=0))
