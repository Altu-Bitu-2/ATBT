from collections import deque

d_do = deque()
d_su = deque()
g_do = []
g_su = []

def bell(d_my, g_my, g_opp): #종 쳤을 때
    d_my.extend(g_opp) #상대방의 그라운드 내 덱에 엎음
    d_my.extend(g_my) #내 그라운드 내 덱어 엎음

n, m = map(int,input().split())

for i in range(n): #카드 숫자 입력받기
    d, s = map(int,input().split())
    d_do.appendleft(d)
    d_su.appendleft(s)
    
for i in range(m):
    
    if i%2 == 0: #도도차례
        g_do.append(d_do.popleft())
        if len(d_do)==0 or len(d_su)==0: #덱의 카드 소진시 종료
            break 
    
        if g_do[-1]==5: #도도가 종침
            bell(d_do, g_do, g_su)
            g_do = []
            g_su = []
        
        if len(g_do)!=0 and len(g_su)!=0 and g_do[-1]+g_su[-1] ==5: #수연이가 종침
            bell(d_su, g_su, g_do)
            g_do = []
            g_su = []
    
    else: #수연이 차례
        g_su.append(d_su.popleft())
        if len(d_do)==0 or len(d_su)==0: #덱의 카드 소진시 종료
            break

        if g_su[-1]==5: #도도가 종침
            bell(d_do, g_do, g_su)
            g_do = []
            g_su = []

        if len(g_do)!=0 and len(g_su)!=0 and g_do[-1]+g_su[-1] ==5: #수연이가 종침
            bell(d_su, g_su, g_do)
            g_do = []
            g_su = []    
            
if len(d_su)>len(d_do) :
    print("su")
elif len(d_su)<len(d_do) :
    print("do")
else:
    print("dosu")