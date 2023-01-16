# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데,
# 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
#
# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

def use_binary_search():
    # 이분 탐색의 기초적인 문제로 이를 이용한 풀이를 하였다.
    # 1. 리스트 A를 정렬
    # 2. 시작 idx를 min, 마지막 idx를 max로 설정
    # 3. min, max를 사용해 중간 idx mid 계산
    # 4. A의 mid 값과 target을 비교
    #   -1 a[mid] == target 일 경우 1 출력
    #   -2 a[mid] => target 일 경우 mid 보다 큰 범위에서 탐색
    #   -3 a[mid] < target 일 경우 mid 보다 작은 범위에서 탐색
    # 5. A[min] > A[max] 경우 -1 출력

    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    arr = list(map(int, input().split()))

    A.sort()

    for i in range(M):
        min = 0
        max = N - 1
        mid = (min + max) // 2

        target = arr[i]

        while min <= max:  # idx가 역전되지 않는 경우 동작
            if A[mid] == target:  # mid값이 target인 경우
                print(1)
                break
            if A[mid] < target:  # mid가 target보다 작은 경우 min값 변경
                min = mid + 1
            else:  # mid가 target보다 작은 경우 max값 변경
                max = mid - 1
            mid = (min + max) // 2
        if min > max:
            print(0)


def use_set():
    # set의 시간 복잡도가 O(1)이라는 점을 착안하여
    # 이분탐색 대신 set을 사용해 문제를 해결해 보았다

    N = int(input())
    A = set(map(int, input().split()))  # input을 set으로 받았다.
    M = int(input())
    arr = list(map(int, input().split()))

    for i in arr:
        if i in A:  # set을 탐색하여 속도 향상
            print(1)
        else:
            print(0)


use_binary_search()
use_set()
