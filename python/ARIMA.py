import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# 生成一个示例时间序列数据
np.random.seed(42)
time_series = np.cumsum(np.random.randn(100))

# 将时间序列转为DataFrame
df = pd.DataFrame(time_series, columns=['Value'])

# 定义一个函数，用于检验时间序列的平稳性
def test_stationarity(timeseries):
    # 使用滑动统计量的方法进行检验
    rolmean = timeseries.rolling(window=12).mean()
    rolstd = timeseries.rolling(window=12).std()

    # 绘制滚动统计量图
    plt.plot(timeseries, label='Original')
    plt.plot(rolmean, label='Rolling Mean')
    plt.plot(rolstd, label='Rolling Std')
    plt.legend()
    plt.show()

    # 进行ADF检验
    result = adfuller(timeseries, autolag='AIC')
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:', result[4])

# 测试时间序列的平稳性
test_stationarity(df['Value'])

# 进行差分，直到时间序列平稳
df['Value_diff'] = df['Value'].diff().dropna()

# 再次测试平稳性
test_stationarity(df['Value_diff'])

# 绘制ACF和PACF图，以确定ARIMA模型的阶数
plot_acf(df['Value_diff'], lags=20)
plt.show()
plot_pacf(df['Value_diff'], lags=20)
plt.show()

# 根据ACF和PACF图的结果选择ARIMA模型的阶数
p, d, q = 1, 1, 1

# 拟合ARIMA模型
model = ARIMA(df['Value'], order=(p, d, q))
results = model.fit()

# 进行未来值的预测
future_steps = 10
forecast = results.get_forecast(steps=future_steps)
forecast_index = np.arange(len(df['Value']), len(df['Value']) + future_steps)

# 绘制原始数据和预测结果
plt.plot(df['Value'], label='Original')
plt.plot(forecast_index, forecast.predicted_mean, color='red', label='Forecast')
plt.fill_between(forecast_index, forecast.conf_int()[:, 0], forecast.conf_int()[:, 1], color='red', alpha=0.3)
plt.legend()
plt.show()
