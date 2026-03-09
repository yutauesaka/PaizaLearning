N, X, Y = map(int, input().split())
string = input()
B = [None]*N
S = [0]*(N+1)

for i in range(N):
    if string[i] == "b":
        B[i] = 1
    else:
        B[i] = 0

for j in range(N):
    S[j+1] = S[j]+B[j]

print(S[Y-1+1]-S[X-1])
