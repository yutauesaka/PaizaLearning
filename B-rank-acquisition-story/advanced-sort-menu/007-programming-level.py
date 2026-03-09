import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

level = 1


def can_solve_all(a, level):
    for problem in a:
        if level >= problem:
            level = problem+1
        else:
            return False

    return True


print("Yes" if can_solve_all(a, level) else "No")
