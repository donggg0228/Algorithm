import sys


def minmult(n, d):

    INF = float('inf')
    M = [[0] * (n + 1) for _ in range(n + 1)]
    P = [[0] * (n + 1) for _ in range(n + 1)]

    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            M[i][j] = INF
            for k in range(i, j):
                cost = M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]
                if cost < M[i][j]:
                    M[i][j] = cost
                    P[i][j] = k

    return M[1][n], M, P


def order(P, i, j):

    if i == j:
        return f"A{i}"
    k = P[i][j]
    left_part = order(P, i, k)
    right_part = order(P, k + 1, j)
    return f"({left_part}{right_part})"


def print_matrix(title, matrix, n):

    print(f"{title} =")
    max_width = max(
        len(str(matrix[i][j]))
        for i in range(1, n + 1)
        for j in range(i, n + 1)
    )
    col_width = max(max_width, 3) + 1

    for i in range(1, n + 1):
        row_str = []
        for j in range(1, n + 1):
            if j < i:
                row_str.append(" " * col_width)
            else:
                row_str.append(f"{matrix[i][j]:>{col_width}}")
        print("".join(row_str).rstrip())


def main():
    first_line = input().strip()
    if not first_line:
        return
    n = int(first_line)

    second_line = input().strip()
    d = list(map(int, second_line.split()))

    # 執行演算法 3.6 計算 M 與 P 矩陣
    _, M, P = minmult(n, d)

    # 輸出 M 矩陣與 P 矩陣
    print_matrix("M", M, n)
    print()
    print_matrix("P", P, n)
    print()

    optimal_solution = order(P, 1, n)
    if optimal_solution.startswith("(") and optimal_solution.endswith(")"):
        optimal_solution = optimal_solution[1:-1]
    print(f"Optimal Solution: {optimal_solution}")


if __name__ == "__main__":
    main()