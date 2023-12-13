import numpy as np

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2],[3,4],[5,6]])
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
d=np.array([[1],[4]])
e=np.array([[1,2,3]])

#矩阵加法
sum = a + b
#矩阵减法
sub = a - b
#元素乘法，对应元素相乘
mul = a * b
#矩阵乘法
dot = np.dot(a,b)
#矩阵求逆
inv = np.linalg.inv(c)
#矩阵转置
e = np.transpose(e)
e = e.T
#矩阵求秩
e = np.linalg.matrix_rank(e)
#矩阵求特征值和特征向量，返回值是一个元组，第一个元素是特征值，第二个元素是特征向量
eig = np.linalg.eig(c)
eigvalues, eigvectors = np.linalg.eig(c)

# 只获取特征值
eigvalues = np.linalg.eig(c)[0]
# 只获取特征向量
eigvectors = np.linalg.eig(c)[1]



