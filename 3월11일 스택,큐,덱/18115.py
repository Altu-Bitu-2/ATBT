n = int(input())
cards = [i+1 for i in range(n)]
new_cards = []

a, b, c, d, e = map(int, input().split())
tech = [a, b, c, d, e]

# 기술에 따라 new_cards에 카드 배치
for i in tech:
    if i == 1:
        new_cards.append(cards[0])
        cards.remove(cards[0])
    elif i == 2:
        new_cards.append(cards[1])
        cards.remove(cards[1])
    elif i == 3:
        new_cards.append(cards[-1])
        cards.remove(cards[-1])

# new_cards는 앞쪽 인덱스부터 들어가서 역정렬        
new_cards.reverse()
dict = {}
# new_cards에 있는 값은 처음 카드의 순서이고 실제 카드에 적혀있는 숫자 배정
for i in range(n):
    dict[new_cards[i]] = i+1
    
sorted_dict = sorted(dict.items(), key=lambda x: x[0]) # 처음 카드의 순서로 정렬
for i in sorted_dict:
    print(i[1], end=' ')