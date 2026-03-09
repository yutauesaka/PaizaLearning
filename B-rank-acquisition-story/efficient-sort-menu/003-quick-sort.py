n = int(input())
A = list(map(int, input().split()))

count = [0]


def quick_sort(A, left, right):
    if left+1 >= right:
        return

    pivot = A[right-1]
    cur_index = left

    for i in range(left, right-1):
        if A[i] < pivot:
            A[cur_index], A[i] = A[i], A[cur_index]
            cur_index += 1
            count[0] += 1

    A[cur_index], A[right-1] = A[right-1], A[cur_index]

    quick_sort(A, left, cur_index)
    quick_sort(A, cur_index+1, right)


quick_sort(A, 0, n)

print(*A)
print(count[0])
