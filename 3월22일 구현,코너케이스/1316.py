n = int(input())
count = 0 #그룹단어가 아닌 단어 카운트

for i in range(n):
    before = [] #전에 나온 거 저장하는 배열
    word = input()
    before.append(word[0]) #제일 첫번째 알파벳 저장
    for j in range(1,len(word)): #두번째부터 검사
        if word[j]==word[j-1]: #직전꺼랑 같으면 넘어감
            continue
        elif word[j] in before: #같은 거 이전에 나왔으면 카운트하고 반복종료
            count +=1
            break
        else: #같은 거 이전에 안 나왔으면 배열에 추가함
            before.append(word[j])
            
print(n-count) #전체 중에 그룹단어 아닌 단어 빼기