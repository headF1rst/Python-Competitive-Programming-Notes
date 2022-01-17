# 주어진 수열
cases = [10, 20, 10, 30, 20, 50]
# LIS의 길이를 위한 LIS배열
memoization = [0]

for case in cases:
    if memoization[-1] < case:
        memoization.append(case)
    else:
        # 이분탐색
        left = 0
        right = len(memoization)
        while left < right:
            mid = (left + right) // 2
            if memoization[mid] < case:
                left = mid + 1
            else:
                right = mid

        memoization[right] = case

# 처음에 들어있던 0을 제외한 나머지 길이 == LIS의 길이
print(len(memoization) - 1)