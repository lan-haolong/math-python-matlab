from sympy import symbols, Eq, solve

# 定义变量
k, b = symbols('k b')
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# 定义方程组
for t in t:
    equation1 = Eq((12/11)*(12-t), 182*k+b)
    equation2 = Eq(1-((12/11)*(12-t)), 184*k+b)

    # 解方程组
    solution = solve((equation1, equation2), (k, b))
    print(f"The solution is: {solution}")
