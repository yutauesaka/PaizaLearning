string = input()
B = [None]*len(string)
S = [0]*(len(B)+1)

for i in range(len(string)):
    if string[i] == "b":
        B[i] = 1
    else:
        B[i] = 0

for j in range(len(B)):
    S[j+1] = S[j]+B[j]

print(S[8-1+1]-S[3-1])
