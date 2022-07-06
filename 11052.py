#11052 카드 구매하기1
#dp

#원하는 카드 개수 입력
N = int(input())

#카드팩 가격 입력. 예를들어 1 5 6 7
p = [0] + list(map(int,input().split()))

# N개의 카드를 구매하기까지의 값들.
dp = [0]*(N+1)

# 1개 최고가, 2개 최고가, ...
# 카드 1개~N개일 때 각 개수 별 매입할 4수 있는 최고가 책정

# 1부터 N까지
for i in range(1,N+1):
    # 예를들면 4개의 최고가를 알아내기 위해 1개, 2개, 3개의 최고가(dp)를 
    # 알아내어 4개의 최고가를 결정
    for j in range(1,i+1):
        # 4개의 최고가를 정하는 데 이전 개수의 최고가가 왜 필요한지는 그림 참고
        # print(i,"의 dp는 ",dp[i])
        dp[i] = max(dp[i], dp[i-j] + p[j]) # i개 살 때의 최고가 구하기
        # print("다시 생각해 본 dp는", dp[i])
print(dp[i])