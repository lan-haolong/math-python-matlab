from scipy.optimize import minimize
import numpy as np
from sympy import symbols, Eq, solve

np.set_printoptions(precision=3, suppress=False)

# 定义变量
k1, b1 = symbols('k1 b1')
k2, b2 = symbols('k2 b2')
k3, b3 = symbols('k3 b3')
k4, b4 = symbols('k4 b4')
t = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
xi = [183.0, 176, 174, 75]
# 定义方程组
for t in t:

    print(f'{t}#############################################{t}')
    def objective(xibest, xi = [183.0, 176.0, 174.0, 75.0]):
        sum1 = 0.0
        sum2 = 0.0
        sum3 = 0.0
        sum4 = 0.0
        global_t = globals()['t']
        for i in range(len(xi)):
            equation1 = Eq(1.0, (xi[i]+1)*k1+b1)
            equation2 = Eq(0.0, (xi[i]-1)*k1+b1)
            solution = solve((equation1, equation2), (k1, b1))
            functionk = solution[k1]*xibest[i]+solution[b1]
            sum1 = sum1 + functionk

        for i in range(len(xi)):
            equation1 = Eq(1.0, (xi[i]-1)*k2+b2)
            equation2 = Eq(0.0, (xi[i]+1)*k2+b2)
            solution = solve((equation1, equation2), (k2, b2))
            functionk = solution[k2]*xibest[i]+solution[b2]
            sum2 = sum2 + functionk

        for i in range(len(xi)):
            if xibest[i] >= xi[i]-1.0 and xibest[i] < xi[i]:
                equation1 = Eq(1.0, xi[i]*k3+b3)
                equation2 = Eq(0.0, (xi[i]-1.0)*k3+b3)
                solution = solve((equation1, equation2), (k3, b3))
                functionk = solution[k3]*xibest[i]+solution[b3]
                sum3 = sum3 + functionk
            else:
                equation1 = Eq(1.0, xi[i]*k3+b3)
                equation2 = Eq(0.0, (xi[i]+1)*k3+b3)
                solution = solve((equation1, equation2), (k3, b3))
                functionk = solution[k3]*xibest[i]+solution[b3]
                sum3 = sum3 + functionk

        for i in range(len(xi)):
            equation1 = Eq(1-global_t/12, (xi[i]-1)*k4+b4)
            equation2 = Eq(global_t/12, (xi[i])*k4+b4)
            solution = solve((equation1, equation2), (k4, b4))
            functionk = solution[k4]*xibest[i]+solution[b4]
            sum4 = sum4 + functionk
        value = sum1*2 + sum2 + sum3*2 + sum4
        return -value


    # initial guesses
    n = 4
    xibest=np.zeros(n)

    cons = []
    bounds = [(182.0, 184.0), (175.0, 177.0), (173.0, 175.0), (74.0, 76.0)]

    solution = minimize(objective, xibest, method='SLSQP', bounds=bounds)

    print(f'最优解{solution.x}')
    print(f'最优值:{-solution.fun}')

