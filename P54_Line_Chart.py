from matplotlib import pyplot as plt
from collections import Counter

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

#한 차트에 여러 개의 선을 그리기 위해 plt.plot을 여러 번 호출할 수 있다.
plt.plot(xs, variance, 'g-', label='variance') #실선
plt.plot(xs, bias_squared, 'g-', label='bias^2') #일점쇄선
plt.plot(xs, total_error, 'g-', label='total error') #점선

#각 선에 레이블을 미리 달아놔서 범례(legend)를 쉽게 그릴 수있다.
plt.legend(loc = 9)
plt.xlabel("model comlexity")
plt.xticks([])
plt.tittle("The Bias-Variance Tradeoff")
plt.show()
