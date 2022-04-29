n = int(input())
s = set()

for i in range(n):
    command = input()
    
    if command == 'all': 
        s.update([j for j in range(1,21)])
    elif command == 'empty':
        s = set()
    else: #숫자를 같이 입력받는 명령들
        command, x = command.split()
        x = int(x)
        if command == 'add':
            s.add(x)
        elif command == 'remove':
            s.remove(x)
        elif command == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.add(x)