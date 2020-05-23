from matplotlib import pyplot as plt
from collections import Counter

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
lables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

#각 포인트에 레이블을 달자,.
for label, friend_count, minute_count in zip(lables, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count), #레이블을 데이터 포인트 근처에 두되
                 xytext=(5, -5),                 # 약간 떨어져 있게 하자.
                 textcoords='offset points')
    
plt.tittle("Daily Minutes vs. Number of Friens")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()
