# dtw_univariate.py
import numpy as np

def dtw_distance(ts1, ts2):
    """
    計算兩條一維時間序列的 DTW 距離及最佳對齊路徑
    :param ts1: list 或 numpy array, 序列1
    :param ts2: list 或 numpy array, 序列2
    :return: dtw_dist (float), path (list of tuple)
    """
    ts1 = np.array(ts1, dtype=float)
    ts2 = np.array(ts2, dtype=float)

    n, m = len(ts1), len(ts2)
    
    # 初始化 DTW 矩陣
    dtw = np.full((n+1, m+1), np.inf)
    dtw[0, 0] = 0

    # 計算累積距離
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(ts1[i-1] - ts2[j-1])
            dtw[i, j] = cost + min(
                dtw[i-1, j],    # insertion
                dtw[i, j-1],    # deletion
                dtw[i-1, j-1]   # match
            )

    dtw_dist = dtw[n, m]

    #最佳路徑回溯
    i, j = n, m
    path = []
    while i > 0 and j > 0:
        path.append((i-1, j-1))
        steps = [(dtw[i-1, j-1], i-1, j-1),
                 (dtw[i-1, j], i-1, j),
                 (dtw[i, j-1], i, j-1)]
        cost_min, i, j = min(steps, key=lambda x: x[0])
    path.reverse()

    return dtw_dist, path


if __name__ == "__main__":
    # 範例測試
    ts1 = [1, 3, 4, 9]
    ts2 = [1, 3, 7, 8, 9]
    
    dist, path = dtw_distance(ts1, ts2)
    print("DTW Distance:", dist)
    print("Alignment Path:", path)

