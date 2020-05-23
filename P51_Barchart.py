from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben_Hue", "Casablacna", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# 막대의 x 좌표는 [0, 1, 2, 3, 4], y좌표는 [num_oscars]로 설정
plt.bar(range(len(movies)), num_oscars)

plt.tittle("My Favorite Movies")
plt.ylabel("# of Academy Awards")

plt.xticks(range(len(movies)), movies)

plt.show()
