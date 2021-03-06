# 백준 11057 오르막 수 / 실버1
# dp

# 첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다. (자리수)
N = int(input())

# 이중 리스트 만들기
dp = [[0]*10 for _ in range(N+1)]

# 첫째 줄(자리수 하나)는 모두 1로 넣기
for i in range(10):
    dp[1][i] = 1

# dp계산 (두 자리 수부터)
for i in range (2, N+1):
    dp[i][0]=1 #맨 뒷자리 수가 0인 경우의 수는 무조건 하나
    for j in range(1, 10):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]

# 첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.
print(sum(dp[N])%10007)
        
