# 정수 N과 K가 입력되었을 때 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# K가 하나라도 포함되는 모든 시각을 세는 프로그램을 작성하시오.
# 시각을 셀 때는 디지털 시계를 기준으로, 초 단위로만 시각을 구분한다.
#
# 예를 들어 K=3일 때, 다음의 시각들은 3이 하나 이상 포함되어 있으므로 세어야 하는 시각의 대표적인 예시이다.
#
# 23시 00분 00초
# 07시 08분 33초
# 반면에 다음의 시각들은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 예시이다.
#
# 15시 02분 55초
# 18시 27분 45초

# 00시 00분 00초부터 N시 59분 59초 동안 k가 포함된 시간의 개수를 세는 문제로
# 3중 for문을 사용해 하나씩 비교하며 개수를 구하였다.
# 반복문 안의 if else문을 사용하지 않을 경우 1:7:3초 같은 경우 0이 제외되므로
# 01:07:03의 형식으로 비교되도록 구현했다.

n, k = map(int, input().split())

cnt = 0

for h in range(n + 1):  # 시간 비교
    if h < 10:  # 1자리 시간일 경우 0H 형식으로 변경
        string_h = '0' + str(h)
    else:
        string_h = str(h)
    for m in range(60):
        if m < 10:
            string_m = '0' + str(m)
        else:
            string_m = str(m)
        for s in range(60):
            if s < 10:
                string_s = '0' + str(s)
            else:
                string_s = str(s)
            if str(k) in string_h + string_m + string_s:
                cnt += 1

print(cnt)
