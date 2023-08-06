# 1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. 
# Ответьте на вопросы:
#   1) Какие вещи взяли все три друга
#   2) Какие вещи уникальны, есть только у одного друга и имя этого друга
#   3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

campaign = {'Sergey': ('tent', 'barbecue', 'matches'),
            'Vadim': ('tent', 'axe', 'lantern'),
            'Oleg': ('sleeping_bag', 'knife', 'compass'),
            }
print(campaign.items())

# 1
all_things = []
for value in campaign.values():
    all_things += value
print(all_things)
print(f"1. Things, that all friens took: {set(all_things)}")

# 2
friends = {}
count = 0
for key, value in campaign.items():
    friends[key] = []
    for j in value:
        for k in all_things:
            if k == j:
                count += 1
        if count == 1:
            friends[key] += [j]
        count = 0

print(f"2. Unic things: {friends}")

#  3
friend_no_thing = []
friends_things = {}
thing = None
counter = 0
for key, value in campaign.items():
    friend_no_thing.append(key)
    friends_things[key] = []
    for j in value:
        if all_things.count(j) > 1:
            friends_things[key] += [j]
            thing = j
            friend_no_thing.remove(key)

print(f"3. {friend_no_thing} doesn't have {thing}" )