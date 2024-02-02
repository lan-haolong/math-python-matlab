import pandas as pd

def normalize_matrix(matrix):
    normalized_matrix = matrix.copy()

    # 获取每个指标的最大值和最小值
    max_values = matrix.max()
    min_values = matrix.min()

    # 确定评价方向，这里假设指标越大越好
    evaluation_direction = 'maximize'

    # 对每个指标进行正向化处理
    for column in matrix.columns:
        if evaluation_direction == 'maximize':
            normalized_matrix[column] = (max_values[column] - matrix[column]) / (max_values[column] - min_values[column])
        else:
            # 如果是越小越好的指标，反向处理
            normalized_matrix[column] = (matrix[column] - min_values[column]) / (max_values[column] - min_values[column])

    return normalized_matrix

# 示例使用
data = X = pd.read_excel(r"E:\A.xlsx", usecols='B:D')

df = pd.DataFrame(data)
print("原始矩阵：")
print(df)

normalized_df = normalize_matrix(df)
print("\n正向化后的矩阵：")
print(normalized_df)
