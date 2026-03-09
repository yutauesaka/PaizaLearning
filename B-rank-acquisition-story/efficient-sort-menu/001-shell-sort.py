n = int(input())
A = list(map(int, input().split()))
k = int(input())
H = list(map(int, input().split()))


def insertion_sort(A, n, h):
    num_of_move = 0
    for i in range(h, n):
        x = A[i]
        j = i-h
        while j >= 0 and A[j] > x:
            A[j+h] = A[j]
            j -= h
            num_of_move += 1
        A[j+h] = x
    print(num_of_move)


for h in H:
    insertion_sort(A, n, h)
