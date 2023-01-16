n = int(input())


def bottom_up(x):
    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 3
    dp[3] = 5

    for i in range(4, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796
    return dp[x]


def top_down(x):
    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 3
    dp[3] = 5

    if dp[x] != 0:
        return dp[x]

    dp[x] = top_down(x - 1) + (top_down(x - 2) * 2) % 796796
    return dp[x]


print(bottom_up(n))
print(top_down(n))
