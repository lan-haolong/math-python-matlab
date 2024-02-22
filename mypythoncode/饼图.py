import matplotlib.pyplot as plt

# 内层饼图数据
labels_inner = ['N', 'S', 'L']
sizes_inner = [0.65707139, 0.19630686, 0.14662175]

# 外层饼图数据
labels_outer = ['TEM', 'WET', 'PM2.5', 'PPD', 'GDP', 'SPC']
sizes_outer = [0.349, 0.449, 0.202, 0.23, 0.42, 0.35]

# 计算内层饼图的起始角度
start_angle_inner = 0

# 绘制内层饼图
fig, ax = plt.subplots()
ax.pie(sizes_inner, labels=labels_inner, autopct='%1.1f%%', startangle=start_angle_inner, colors=['skyblue', 'lightgreen', 'lightcoral'])
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# 计算外层饼图的起始角度
start_angle_outer = start_angle_inner + 360

# 绘制外层饼图
ax.pie(sizes_outer, labels=labels_outer, autopct='%1.1f%%', startangle=start_angle_outer, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightsalmon', 'lightpink'])
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Double-layer Pie Chart')
plt.show()
