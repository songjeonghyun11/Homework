users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
]

friendship_paris = { (0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
                    (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)}

friendships = {user["id"]: [] for user in users}
#사용자별로 비어 있는 친구 목록 리스트를 지정하여 딕셔너리를 초기화

for i, j in friendship_paris:
    friendships[i].append(j) # j를 사용자 i의 친구로 추가
    friendships[j].append(i) # i를 사용자 j의 친구로 추가

def number_of_friends(user):
    """user의 친구는 몇 명일까?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user)
                    for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

# (user_id, number_of_friends)로 구성된 리스트 생성
num_friends_by_id = [(user["id"], number_of_friends(user))
                    for user in users]

num_friends_by_id.sort(  #정렬
    key = lambda id_and_friends: id_and_friends[1], #num_firends 기준으로
    reverse=True)                                   #제일 큰숫자부터 작은 숫자순으로

#친구 추천 기능
def foaf_ids_bad(user):
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

# 서로 아는 친구수와 사용자가 이미 아는 사람을 제외하는 함수

from collections import Counter

def friends_of_friend(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id] #사용자의 친구 개개인에 대해
        for foaf_id in friendships[friend_id] # 그들의 친구들을 세어보고
        if foaf_id != user_id                 # 사용자 자신과
        and foaf_id not in friendships[user_id] # 사용자의 친구제외
    )
