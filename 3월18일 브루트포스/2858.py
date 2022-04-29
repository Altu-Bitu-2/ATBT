r, b = map(int,input().split())

area = r + b #전체넓이는 타일의 합
pairs = []

for i in range(3,area):
    if area%i == 0 and area/i >= 3: #brown타일이 1이상이므로 가로세로 모두 3이상
        pairs.append((i,area//i))

def tiles(area, pair):
    red = pair[0]*2 + pair[1]*2 -4
    brown = area - red
    return [red,brown]
        
answer = []
for i in pairs:
    if tiles(area, i) == [r,b]: #입력과 같으면 답
        answer.append(i)
        
answer.sort(reverse=True) #튜플의[0]으로 정렬되는데. 반대로 정렬
print(answer[0][0], answer[0][1])