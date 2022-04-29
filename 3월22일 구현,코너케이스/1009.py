import sys
input = sys.stdin.readline

n = int(input())

def print_remain(a,b): 
    remains = []

    for i in range(1,b+1): #반복되는 나머지들이 저장됩니다
        temp = (a**i)%10
        if temp in remains : #같은 수를 만나면 반복이 끝납니다
            break
        else:
            remains.append(temp)
            
    if b%len(remains) == 0: #나누어 떨어지면 마지막 수
        print(remains[-1])
    else:
        print(remains[b%len(remains)-1]) #아니면 앞에꺼, 위에서 1부터 돌렸기 때문에

for i in range(n):
    a, b = map(int,input().split())
    
    if a%10 == 0: #10의 배수라면 0이 나오니까 10번 컴퓨터
        print(10)
    else:
        print_remain(a,b)