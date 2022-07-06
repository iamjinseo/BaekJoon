# 백준 10844 쉬운 계단 수 / 실버1
# dp

# 인접한 모든 자리 차이가 1이 나는 계단 수 만들기
# N이 주어질 때 길이가 N인 계단 수가 몇 개 있을까?

# 첫째 줄에 N이 주어진다. N은 1이상 100이하
N = int(input())

# 이중 리스트 만들기
dp = [[0]*10 for _ in range(N+1)]

# 자리수가 하나일 때의 경우 집어넣기
for i in range(1, 10):
    dp[1][i] = 1

# 자릿수에 따라, 0~9까지의 수가 맨 뒤에 올 수 있는경우의 수 구하기
for i in range(2, N+1):
    for j in range(0, 10):
        if j==0 : 
            dp[i][j]=dp[i-1][1]
        elif j==9:
            dp[i][j]=dp[i-1][8]
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]

#첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
print(sum(dp[N])%1000000000)