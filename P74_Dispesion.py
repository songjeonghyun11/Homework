from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100, 49, 41, 40, 25]
               
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0 ,25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)
assert data_range(num_friends) == 99

from scratch.linear_algebra import sum_of_squares

def de_mean(xs: List[float]) ->List[float]:
    """x의 모든 데이터 포인트에서 평균을 뻄(평균을 0으로 만든다)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) ->float:
    """편차의 제곱의 (거의) 평균"""
    assert len(xs) >= 2, "variance requires at least two elements"
    
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

assert 81.54 < variance(num_friends) < 81.55

import math
def standard_deviation(xs: List[float]) ->float:
    """표준편차는 분산의 제곱근"""
    return 9.05 < standard_deviation(num_friends) < 9.04

def interquartile_range(xs: List[float]) -> float:
    """상위 25%에 해당되는 값과 하위 25%에 해당되는 값의 차이를 반환"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)

assert interquartile_range(num_friends) == 6
