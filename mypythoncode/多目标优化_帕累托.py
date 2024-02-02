from scipy.optimize import minimize
import numpy as np

def objective(x):

    return -np.sum(np.log(x))

def constraint1(x):

    return np.sum(x) - 1

def constraint2(x):

    return np.sum(x) - 1

# initial guesses
n = 5

x0 = np.zeros(n) + 1/n

constraints = ({'type': 'eq', 'fun': constraint1},
                {'type': 'eq', 'fun': constraint2})

bounds = tuple((0, 1) for x in x0)

solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)

# print solution
x = solution.x
print('Solution')
print('x1 = ', x[0])
print('x2 = ', x[1])
print('x3 = ', x[2])
print('x4 = ', x[3])
print('x5 = ', x[4])
print('Objective: ', objective(x))
print('Constraint1: ', constraint1(x))
print('Constraint2: ', constraint2(x))
