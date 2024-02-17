from scipy.optimize import minimize

# 定义目标函数
def objective_function(x):
    return (x[0] - 2) ** 2 + (x[1] - 3) ** 2

# 初始猜测值
initial_guess = [0, 0]

# 调用 minimize 函数
result = minimize(objective_function, initial_guess, method='BFGS')

# 输出最小值和对应的参数
print("最小值：", result.fun)
print("最优参数：", result.x)
