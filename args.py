import sys
'''명령행 인지값 확인용 모듈'''

args = sys.argv[1:]
print(f'현재 구동중인 프로그램은 : {sys.argv[0]}')
for x in args:
    print(x, end=' ')
else:
    print()
