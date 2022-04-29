from itertools import combinations as combi

n, m = map(int,input().split())
numbers = list(map(int,input().split()))

combi_list = list(combi(numbers,3)) #조합을 이용해 가능한 숫자 조합을 모두 찾습니다

combi_sum = []
for i in combi_list:
    combi_sum.append(sum(i)) #각 조합 수들의 합을 리스트에 저장합니다
    
combi_sum.sort(reverse=True) #합을 내림차순으로 정렬합니다
for i in combi_sum:
    if i <= m: #숫자가 m보다 작거나 같아지는 순간 출력하고 반복을 멈춥니다
        print(i)
        break