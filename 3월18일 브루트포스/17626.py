from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
if n**(1/2) == int(n**(1/2)): #제곱수이면 1반환
    print(1)
else:
    square_numbers = []
    for i in range(n,0,-1): #n보다 작은 모든 제곱수를 구합니다
        if i**(1/2) == int(i**(1/2)):
            square_numbers.append(i)

    answer = 4 #아래꺼 돌렸는데 안나오면 답은 4
    for i in range(2,4): #2개 또는 3개로 조합해 합이 n이 나오면 답이 나옵니다
        combi = list(combinations(square_numbers,i)) 
        for j in combi:
            if sum(j) == n:
                answer = i
                break            
        if answer != 4:
            break
                
    print(answer)