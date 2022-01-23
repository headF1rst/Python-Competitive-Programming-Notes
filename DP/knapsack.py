# 배낭의 최대 무게
beg_weight = 5

# 보석의 무게, 가치
dia_weight = [2, 1, 4, 3]
dia_value = [4, 1, 3, 2]
dia = [(0, 0)]

for i in range(len(dia_weight)):
    dia.append((dia_weight[i], dia_value[i]))

# 보석의 최대 가치 메모를 위한 dp
dp = [[0] * (beg_weight + 1) for _ in range(len(dia))]

print(len(dp))

for i in range(1, len(dia)):
    cdw = dia[i][0]    # i 번째 보석 무게
    cdv = dia[i][1]    # i 번째 보석 가치

    for cbw in range(1, beg_weight + 1):
        # 배낭의 최대 무게가 보석의 무게보다 작아서 담지 못하는 경우
        if cbw < cdw: dp[i][cbw] = dp[i - 1][cbw]
        # i 번째 보석을 넣는 경우와 그렇지 않는 경우의 최적 해를 비교
        else: dp[i][cbw] = max(dp[i - 1][cbw], dp[i - 1][cbw - cdw] + cdv)

# 배낭의 최대 무게에 대한 최대 가치 출력
print(dp[len(dia) - 1][beg_weight])