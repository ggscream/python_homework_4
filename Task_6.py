# Задача из Яндекса: https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/Z4TZboVPOx

friend_paires = []
names = set()

while (text := input()) != "":
    temp = text.split()
    for i in temp:
        names.add(i)
    friend_paires.append(temp)

names = list(names)
names.sort()

for i in names:
    friends = []
    second_friends = []
    for j in friend_paires:
        for k in range(len(j)):
            if i == j[k]:
                friends.append(j[k - 1])
    for j in friends:
        for k in friend_paires:
            for n in range(len(k)):
                if j == k[n]:
                    if k[n - 1] != i:
                        second_friends.append(k[n - 1])
    second_friends = list(set(second_friends) - set(friends))
    second_friends.sort()
    final_line = f"{i}: "
    for j in range(len(second_friends)):
        if j != len(second_friends) - 1:
            final_line += f"{second_friends[j]}, "
        else:
            final_line += f"{second_friends[j]}"
    print(final_line)