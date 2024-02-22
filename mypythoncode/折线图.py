import matplotlib.pyplot as plt

# 示例数据
x_values = [100, 90, 80, 70, 60, 50]
y_values = [0.0082, 0.009, 0.0264, 0.5522, 0.024, 0.0096]

# 创建折线图
plt.plot(x_values, y_values, linewidth=3)
#label='Sensitivity Analysis'
# 添加标题和标签
plt.title('Sensitivity Analysis')
plt.xlabel('Number of Hidden Layers in a Neural Network')
plt.ylabel('Error(%)')

# 添加图例
plt.legend()

# 显示图形
plt.show()
