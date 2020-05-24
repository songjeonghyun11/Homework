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

