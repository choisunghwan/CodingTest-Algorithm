# N 입력받기
n=int(input())
x, y=1, 1
plans = input().split()

dx = [0,0,-1,51]
dy = [-1,1,0,0]
move_types=['L','R','U','D']

# 이동 계획을 하나씩 확인하기 / 입력받은 R 또는 L U D 에 대해 하나씩 값을 plan에 저장
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)): # move_type의 길이는 4개이다.(0~3)
        if plan == move_types[i]: # i 가 0 일때 L을 의미. 1일때는 R... 입력받은 값중 하나와 move_type이 같다면 아래 코드 실행
            nx=x+dx[i]
            ny=y+dy[i]
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny<1 or nx > n or ny > n:
        continue
    # 이동 수행 
    x,y=nx,ny
print(x, y)