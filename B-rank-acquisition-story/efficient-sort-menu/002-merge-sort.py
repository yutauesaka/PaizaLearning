n = int(input())
A = list(map(int, input().split()))

count = [0]


def merge(A, left, mid, right):

    nl = mid-left
    nr = right-mid

    L = [None]*(nl+1)
    R = [None]*(nr+1)

    for i in range(nl):
        L[i] = A[left+i]
    for i in range(nr):
        R[i] = A[mid+i]

    L[nl] = 10**18
    R[nr] = 10**18

    lindex = 0
    rindex = 0

    for i in range(left, right):
        if L[lindex] < R[rindex]:
            A[i] = L[lindex]
            lindex += 1
        else:
            A[i] = R[rindex]
            rindex += 1
            count[0] += 1


def merge_sort(A, left, right):
    if left+1 < right:
        mid = (left+right)//2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


merge_sort(A, 0, n)

print(*A)
print(count[0])
