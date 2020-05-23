from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#x축에 연도, y축에 GDP가 있는 석ㄴ그래프를 만들자.
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# 제목을 더하자.
plt.tittle("Nominal GDP")

# y축에 레이블을 추가하자.
plt.ylable("Billions of $")
plt.show()
