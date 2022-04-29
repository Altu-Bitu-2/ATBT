a, b = input().split()

#자릿수를 맞춰줍니다
if len(a)>len(b):
    zeros = '0'*(len(a)-len(b))
    b = zeros + b
elif len(b)>len(a):
    zeros = '0'*(len(b)-len(a))
    a = zeros + a

result = []
next_sum = 0 #더했을 때 10보다 크면 1을 더해주기 위한 변수
for i in range(len(a)-1, -1, -1): #일의자리부터 더하기 위해 역순
    sum = int(a[i]) + int(b[i]) + next_sum
    next_sum = 0 #다음 반복을 위해 초기화
    if i == 0: #마지막에는 수가 10보다 크면 그대로 반환
        result.append(str(sum))
    else:
        result.append(str(sum)[-1])
        
    if sum > 9:
        next_sum = 1

result.reverse()
print(''.join(result))