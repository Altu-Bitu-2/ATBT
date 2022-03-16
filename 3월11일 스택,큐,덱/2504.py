list = input()

false = 0 #틀린 괄호열

# 괄호열의 길이가 홀수이거나, 괄호열 시작이 닫는 괄호 혹은 괄호열 끝이 여는 괄호
if len(list)%2 != 0 or list[0]== ')' or list[0]==']' or list[-1]=='(' or list[-1]=='[':
    false += 1

# 여는 괄호의 개수와 닫는 괄호의 개수가 다를 때 
if list.count('(') != list.count(')') or list.count('[') != list.count(']'):
    false += 1

# (])[ 같은 경우
for i in range(len(list)-1):
    if list[i] == '(' and list[i+1]==']':
        false += 1
    elif list[i] == '[' and list[i+1]==')':
        false += 1
        

cul = [] #계산결과

for i in range(len(list)-1):
    # 여는 괄호가 연속으로 나오면 곱해줌
    if list[i] == '(' and list[i+1]=='(':
        cul.append('2*(')
    elif list[i] == '(' and list[i+1]=='[':
        cul.append('2*(')
    elif list[i] == '[' and list[i+1]=='(':
        cul.append('3*(')
    elif list[i] == '[' and list[i+1]=='[':
        cul.append('3*(')
    # 같은 괄호가 바로 닫히면 그냥 숫자
    elif list[i] == '(' and list[i+1]==')':
        cul.append('(2')
    elif list[i] == '[' and list[i+1]==']':
        cul.append('(3')
    # 닫는 괄호가 연속으로 나오면 괄호닫기
    elif list[i] == ')' and list[i+1]==')':
        cul.append(')')
    elif list[i] == ')' and list[i+1]==']':
        cul.append(')')
    elif list[i] == ']' and list[i+1]==')':
        cul.append(')')
    elif list[i] == ']' and list[i+1]==']':
        cul.append(')')
    # 닫는 괄호 다음에 바로 여는 괄호가 나오면 더해줌
    elif list[i] == ')' and list[i+1]=='(':
        cul.append(')+')
    elif list[i] == ')' and list[i+1]=='[':
        cul.append(')+')
    elif list[i] == ']' and list[i+1]=='(':
        cul.append(')+')
    elif list[i] == ']' and list[i+1]=='[':
        cul.append(')+')
        
cul.append(')') # 마지막괄호 닫기
cul_str = ''.join(cul) # 리스트를 문자열로 만들기

if false == 0:
    print(eval(cul_str)) # 문자열을 계산해주는 함수
else:
    print(0)