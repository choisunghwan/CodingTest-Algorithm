# <그리디 문제>1이 될 때까지 

#N,K 을 공백을 기준으로 구분하여 입력받기
n,k = map(int, input().split())

result =0

while True:
  #N이 K로 나누어 떨어지는 수가 될때 까지 빼기
  target = (n // k) * k
  result += (n - target)
  n=target
  #N이 K 보다 작을때 (더 이상 나눌 수 없을때) 반복문 탈출
  if n < k:
    break
  #k 로 나누기
  result+=1
  n//=k

result +=(n-1)
print(result)