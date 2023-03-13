S = str(input())

ans = 0

for i in range(0, len(S)-1):
    if S[i] != S[i-1]:
        ans += 1

print((ans+1)//2)
