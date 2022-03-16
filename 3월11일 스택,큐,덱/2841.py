import sys
input = sys.stdin.readline

n, p = map(int, input().split())

dict = {1:[0], 2:[0], 3:[0], 4:[0], 5:[0], 6:[0]} # 각 줄별로 리스트가 있는 딕셔너리
count = 0


for i in range(n):
    line, pr = map(int, input().split())
    
    # 이 음을 짚고있고 더 높은 음도 짚고있는 경우
    if pr in dict[line] and max(dict[line]) > pr: 
        while(max(dict[line]) > pr):
            count += 1
            dict[line].remove(max(dict[line]))
    # 이 음을 짚고있고 이 음이 가장 높은 음인 경우
    elif pr in dict[line] and max(dict[line]) == pr:
        count += 0
    # 이 음을 짚지 않고 더 높은 음을 짚고있는 경우
    elif pr not in dict[line] and max(dict[line]) > pr:
        while(max(dict[line]) > pr): 
            count += 1
            dict[line].remove(max(dict[line]))
            
        dict[line].append(pr)
        count += 1
    # 이 음을 짚지 않고 더 높은 음은 없는 경우
    elif pr not in dict[line] and max(dict[line]) < pr:
        count += 1
        dict[line].append(pr)

    
print(count)