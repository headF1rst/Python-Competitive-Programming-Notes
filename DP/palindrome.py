# 수열의 크기 n
n = int(input())

# 팰린드롬인지 확인할 숫자들
numbers = [0] + list(map(int, input().split()))

# 팰린드롬 확인할 횟수
m = int(input())

# dp[s][e] = numbers의 s부터 e까지가 팰린드롬이면 1, 아니면 0
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for start in range(1, n + 1 - i):
        end = start + i

        # 숫자 하나를 검사하는 경우
        if start == end:
            dp[start][end] = 1
        # 펠린드롬 측정 시작과 끝이 같은 경우
        elif numbers[start] == numbers[end]:
            # 1 1과 같이 측정 길이가 2이고 앞 뒤가 같은경우
            if start + 1 == end:
                dp[start][end] = 1
            # start와 end값이 같고, 그 사이의 수가 펠린드롬이면 펠린드롬
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])
