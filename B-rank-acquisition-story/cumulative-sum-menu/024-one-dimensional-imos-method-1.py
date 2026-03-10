numbers = [0]*10
starts = [1, 1, 3, 3, 7]
ends = [3, 8, 8, 6, 9]
S = [0]*(10+1)

# starts[i]とends[i]を0-indexedに変換してから
# 区間の始まりと終わり+1にそれぞれ1,-1を足す
for i in range(5):
    starts[i] -= 1
    ends[i] -= 1
    numbers[starts[i]] += 1
    numbers[ends[i]+1] -= 1

# numbersの累積和をとる
for j in range(len(numbers)):
    S[j+1] = S[j]+numbers[j]

# Sの最大値をとる
print(max(S))
