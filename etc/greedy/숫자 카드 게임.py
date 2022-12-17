# 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
# 게임의 룰을 지켜야 하며 룰은 다음과 같다.
# 1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. 이때 N은 행의 개수, M은 열의 개수를 의미한다.
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 4. 각 행에서 고른 카드들 중 가장 큰 숫자인 가트를 선택한다.

# 문제에서 풀이 방법을 사실상 준 문제로
# min 함수를 사용해서 행에서 가장 작은 숫자의 카드를 선택하고
# max 함수를 사용해서 열의 개수 만큼 비교하여 가장 큰 카드를 선택하도록 구현했다.

n, m = map(int, input().split())

result = 0

for i in range(n):
    numbers = list(map(int, input().split()))
    min_number = min(numbers)   # 행에서 가장 작은 숫자를 선택
    result = max(result, min_number)    # result 값과 선택한 작은 수 중 큰 숫자를 result에 대입한다.

print(result)
