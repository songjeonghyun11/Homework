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

num_points = len(num_friends) #204 포인트 개수

largest_value = max(num_friends) #100 최댓값
smallest_value = min(num_friends) #1 최솟값

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

def mean(xs: List[float]) -> float: #데이터의 중심이 어디 있는 지를 나타내는
    return sum(xs) / len(xs)        # 중심 경향성 지표
mean(num_friends) #7.333333

#밑줄 표시로 시작하는 함수는 프라이빗 함수를 의미하며,
# median 함수를 사용하는 사람이 직접 호출하는 것이 아닌
# median 함수만 호출하도록 생성되었다.

def _median_even(xs: List[float]) -> float:
    """len(xs)가 홀수면 중앙값을 반환"""
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
    """len(xs)가 짝수면 두 중앙값의 평균을 반환"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2 # e.g. length 4 => hi_midpoint 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
    """v의 중앙값을 계산"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

print(median(num_friends)) #6 사용자별 친구 수의 중앙값

def quantile(xs: List[float], p: float) -> float:
    """x의 p분위에 속하는 값을 반환"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

assert quantile(num_friends, 0.10) == 1
assert quantile(num_friends, 0.25) == 3
assert quantile(num_friends, 0.75) == 9
assert quantile(num_friends, 0.90) == 13

def mode(x: List[float]) -> List[float]:
    """최빈값이 하나보다 많을수도 있으니 결과를 리스트로 반환"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

assert set(mode(num_friends)) == {1, 6}
