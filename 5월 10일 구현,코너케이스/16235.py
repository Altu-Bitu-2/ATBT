import sys
from collections import deque #덱 이용
input = sys.stdin.readline #입력속도 줄임

"""
 [문제 설명] - 단순 구현 문제
 봄: 하나의 칸마다 나이가 어린 나무부터 자신의 나이만큼 양분을 먹고, 나이가 1 증가함
    각 칸에 양분이 부족해 자신의 나이만큼 양분을 못 먹는 나무는 즉시 죽음
 여름: 봄에 죽은 나무가 양분으로 변함. 죽은 나무마다 나이를 2로 나눈 값이 양분으로 추가 (소수점 버림)
 가을: 나이가 5의 배수인 나무가 번식. 인접한 8개 칸에 나이가 1인 나무가 생김
 겨울: 로봇(S2D2)이 땅을 돌아다니면서 A[r][c]만큼 각 칸에 양분 추가

 K년이 지난 후 상도의 땅에 살아있는 나무의 개수

 [문제 풀이]
 a: 로봇(S2D2)가 겨울에 주는 양분의 양
 land: 땅의 현재 양분 상태
 tree[i][j]: 해당 영역에 존재하는 나이와 개수를 튜플로 묶어서 덱에 저장
 - 새로운 나무가 번식하기 때문에, 나이에 대한 오름차순을 유지하기 위해서는 앞에서의 삽입이 필요

"""

# 봄을 거쳐 나이를 먹은 나무들에 의해 새롭게 태어나게 되는 나무의 수를 계산
def breeding(breeding_src):
    dr = [-1, -1, -1, 0, 0, 1, 1, 1] #8개의 주변 칸에 새로운 나무가 생김
    dc = [-1, 0, 1, -1, 1, -1, 0, 1] #8개의 주변 칸에 새로운 나무가 생김

    breeding_cnt = [[0]*n for _ in range(n)] #새로운 나무의 수 초기화

    for r in range(n): #row 반복
        for c in range(n): #col 반복
            if breeding_src[r][c] == 0: #번식할 나무가 없다면
                continue #넘어감
            for i in range(8): #번식할 나무가 있다면 8개의 주변 칸에 반복
                nr = r+dr[i] #주변 칸의 row값
                nc = c+dc[i] #주변 칸의 col값
                if 0 <= nr < n and 0 <= nc < n: #주변 칸이 전체 땅을 넘어가지 않을 때
                    breeding_cnt[nr][nc] += breeding_src[r][c] #새로운 나무의 수 더해줌

    return breeding_cnt #새로운 나무의 수 출력

# 봄과 여름을 묶어서 진행
def spring_summer():
    breeding_src = [[0]*n for _ in range(n)]    # 나이가 5의 배수가 되어 가을에 번식을 하는 나무의 수를 각 영역에 저장

    for i in range(n): #행반복
        for j in range(n): #열반복
            next_year = deque() #다음해의 덱을 저장
            dead = 0 #죽는 나무의 수

            while tree[i][j]: #i,j칸에 나무가 있을 때
                age, cnt = tree[i][j].popleft() #있는 나무를 하나씩 꺼냄
                # 해당 나이의 모든 나무에게 양분을 줄 수 없는 경우
                if land[i][j] < age * cnt:  #양분이 더 적을 때
                    dead = cnt - land[i][j] // age #죽는 나무 수
                    cnt = land[i][j] // age # 살 수 있는 최대 수

                if cnt > 0: #살 수 있는 나무가 있을 때
                    land[i][j] -= age * cnt #양분 적어짐
                    next_year.append((age+1, cnt)) #나무의 나이 추가해서 저장

                    if (age + 1) % 5 == 0: #번식하는 나무라면
                        breeding_src[i][j] += cnt #번식하는 나무라고 표시함

                # 죽은 나무가 생기면 그 이후의 나무는 모두 죽게 된다.
                if dead > 0: #하나라도 죽었을 때
                    land[i][j] += (age // 2) * dead # 여름에 양분이 됨
                    break #반복 멈춤
            
            # 여름 -> 죽은 나무들이 양분이 됨
            while tree[i][j]: #값이 존재할 때
                age, dead = tree[i][j].popleft() #나이와 죽은 횟수
                land[i][j] += (age // 2) * dead #양분에 추가됨

            tree[i][j] = next_year #내년의 상태로 바꿈

    return breeding_src #번식할 나무들 출력

def autumn_winter(breeding_src): #가을, 겨울
    # 봄에 나이를 먹은 나무들의 번식 결과
    breeding_cnt = breeding(breeding_src) #봄,여름을 거쳐 나온 번식할 나무들에 대한 정보를 입력해 새롭게 태어날 나무의 수를 저장

    for i in range(n): #행반복 
        for j in range(n): #열반복
            # 가을 - 번식
            if breeding_cnt[i][j]: #새롭게 태어날 나무의 수 꺼내옴
                tree[i][j].appendleft((1, breeding_cnt[i][j])) #각 칸에 1살인 나무 추가
            # 겨울 - 로봇에 의해 양분 추가
            land[i][j] += winter_list[i][j] #입력으로 받은 추가할 양분 리스트 추가
    return #종료


# 입력
n, m, k = map(int, input().split()) #입력받음
winter_list = [list(map(int, input().split())) for _ in range(n)] #겨울에 추가될 양분의 정보를 저장한다

land = [[5]*n for _ in range(n)] #처음에는  모두 양분이 5
tree = [[deque() for _ in range(n)] for _ in range(n)]  # -> 만약 여기서 [deque()] * n으로 하면 어떻게 될까요?

for _ in range(m): #m개의 나무
    x, y, z = map(int, input().split()) #나무 정보 입력받음
    tree[x-1][y-1].append((z, 1)) #나무 위치에 나무 나이 저장


# k년 동안 시뮬레이션
for _ in range(k): #k번 반복
    breeding_src = spring_summer() #봄,여름 시뮬레이션
    autumn_winter(breeding_src) #가을,겨울 시뮬레이션

ans = 0 #정답 초기화

# 남아 있는 나무 수 카운트
for line in tree: #전체 탐색을 위해 반복
    for area in line: #전체 탐색을 위해 반복
        for _, cnt in area: #area의 cnt로 반복
            ans += cnt #ans에 더해줌

print(ans) #정답 출력