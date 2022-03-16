from collections import Counter

n = int(input())

num_list = []
for i in range(n):
    num_list.append(int(input()))
    
num_list.sort() # 중앙값때문에 정렬
    
count = Counter(num_list)
mode_list = []

for i in count.items():
    if i[1] == max(count.values()): # 최빈값인 것들 모으기, 여러 개면 두 번째로 작은 거 출력해야 함
        mode_list.append(i)

mode = int()
if len(mode_list) == 1: # 최빈값인 것이 한 개일 때
    mode = mode_list[0][0]
else: # 최빈값인 것이 여러 개일 때
    mode_list.sort() 
    mode = mode_list[1][0]
    
print(round(sum(num_list)/n)) #평균
print(num_list[round(n/2)]) #중앙값
print(mode) #최빈값
print(max(num_list)-min(num_list)) #범위