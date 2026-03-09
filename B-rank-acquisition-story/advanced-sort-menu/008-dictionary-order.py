K = int(input())
strings = []
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# 辞書順に文字列を作る
for i in range(26):
    for j in range(26):
        for k in range(26):
            strings.append("".join([alphabets[i], alphabets[j], alphabets[k]]))

# 0-indexedに変換
K -= 1

print(strings[K])
