# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.


# 간단한 정렬 문제로 sorted를 사용해 오름차순 결과를 출력했다.

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# array를 오름차순 정렬
array = sorted(array)

for i in array:
    print(str(i) + ' ')
