def recursive_function(i):
    #100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return

    # 1~ 99 번째 까지     
    print(i,'번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1) #재귀함수 호출
    print(i, '번째 재귀함수를 종료합니다.')



recursive_function(1)  # i 값은 1로 설정하였음.


# 스택 구조임을 확인 할 수 있다.