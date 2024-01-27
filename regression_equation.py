import numpy as np

# データ
height = np.array([191, 193, 190, 179, 183, 188, 190, 179, 181, 188, 187, 186, 177, 178, 178, 174, 172, 180, 176, 171, 173, 176, 182, 177, 173, 173])
weight = np.array([86, 90, 98, 69, 75, 80, 84, 69, 76, 84, 84, 80, 74, 76, 73, 68, 70, 73, 66, 70, 64, 67, 76, 69, 71, 67])

# データの数
n = len(height)

# 各種統計量の計算
sum_x = np.sum(height)
sum_y = np.sum(weight)
sum_xy = np.sum(height * weight)
sum_x_squared = np.sum(height**2)

# 最小二乗法による回帰係数の計算
b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
b0 = (sum_y - b1 * sum_x) / n

# 回帰方程式の表示
print(f'回帰方程式: 体重 = {b0:.2f} + {b1:.2f} * 身長')

# 結果の表示
print(f'切片 (b0): {b0:.2f}')
print(f'傾き (b1): {b1:.2f}')
