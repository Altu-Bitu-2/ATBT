# 숫자야구 함수(예상숫자, 정답숫자)
def baseball(q, a):
    a_list = list(str(a)) # 정답숫자로 들어오는 int를 비교를 위해 list로 변환
    strike = 0
    ball = 0
    for i in range(len(a_list)):
        if q[i] == a_list[i]:
            strike += 1
        elif q[i] in a_list:
            ball +=1
            
    return [strike, ball]

n = int(input())
answer = set(i for i in range(111,1000))

# 0이 들어있는 수들을 지웁니다
zero = set()
for i in answer:
    i_list = list(str(i))
    if '0' in i_list:
        zero.update([i])

answer = answer - zero

# 서로 같은 수가 있는 수들을 지웁니다
same_number = set()
temp = [str(i) for i in range(1,10)]
for i in answer:
    i_list = list(str(i))
    for j in temp:
        if i_list.count(j) > 1:
            same_number.update([i])

answer = answer - same_number

# 테스트 숫자와 결과가 다른 수들을 지웁니다
diff = set()
for i in range(n):
    q, s, b = input().split()
    q = list(q)
    sb_list = [int(s), int(b)]
    
    for j in answer:
        if baseball(q, j) != sb_list:
            diff.update([j])
            
answer = answer - diff
                
print(len(answer))