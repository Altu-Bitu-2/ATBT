from collections import Counter
from collections import deque

deq = deque()

word = sorted(input(), reverse = True)
dict = Counter(word) #각 알파벳의 수를 셈
odd_count = 0 #홀수개인 알파벳의 수
odd = ''

for i in dict.items():
    if odd_count > 1: #홀수개인 알파벳이 한개 이상이면 실패
        break
    
    if i[1]%2 !=0: #알파벳이 홀수개일 때 한개 빼놓기
        odd_count += 1
        odd = i[0]
        word.remove(i[0])
        
if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    deq.append(odd) #홀수개인 알파벳은 한개가 중간으로 들어감

    for i in range(len(word)) : #나머지는 모두 짝수개이고 앞뒤에 차례로 붙음
        if i%2 == 0:
            deq.append(word[i])
        else:
            deq.appendleft(word[i])
        
    result = ''.join(list(deq))
    print(result)