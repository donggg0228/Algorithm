import sys


def floyd(n, W):
    INF = float('inf')

    # 初始化距離矩陣 D = W，將 -1 轉換為無限大 (INF)
    D = [[INF if val == -1 else val for val in row] for row in W]

    # 核心三重迴圈：依序將頂點 k 作為中繼點，更新所有頂點對 (i, j) 的最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]

    return D


def main():
    # 讀取第一行：圖形的頂點數
    first_line = sys.stdin.readline().strip()
    if not first_line:
        return
    n = int(first_line)

    # 讀取第二行及其後的相鄰矩陣 W（矩陣一列一文字行，元素以一個或多個空白字元隔開）
    W = []
    while len(W) < n:
        line = sys.stdin.readline()
        if not line:
            break
        row = list(map(int, line.split()))
        if row:  # 略過多餘的空行
            W.append(row)

    # 計算最短距離矩陣 D
    D = floyd(n, W)

    # 輸出最短距離矩陣 D（矩陣一列一文字行，元素以一個空白字元隔開）
    for row in D:
        print(' '.join(str(-1 if val == float('inf') else int(val)) for val in row))


if __name__ == '__main__':
    main()