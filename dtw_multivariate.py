# dtw_multivariate.py
import numpy as np

def dtw_distance_multivariate(ts1, ts2):
    """
    計算兩條多維時間序列的 DTW 距離及最佳對齊路徑
    :param ts1: numpy array, shape=(n, d)，n為時間點數，d為維度
    :param ts2: numpy array, shape=(m, d)
    :return: dtw_dist (float), path (list of tuple)
    """
    ts1 = np.array(ts1, dtype=float)
    ts2 = np.array(ts2, dtype=float)
    
    n, d1 = ts1.shape
    m, d2 = ts2.shape
    assert d1 == d2, "兩序列維度必須一致"

    # 初始化 DTW 矩陣
    dtw = np.full((n+1, m+1), np.inf)
    dtw[0, 0] = 0

    # 計算累積距離
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 使用 Euclidean distance 作為局部距離
            cost = np.linalg.norm(ts1[i-1] - ts2[j-1])
            dtw[i, j] = cost + min(
                dtw[i-1, j],    # insertion
                dtw[i, j-1],    # deletion
                dtw[i-1, j-1]   # match
            )

    dtw_dist = dtw[n, m]

    # 回溯找到最佳對齊路徑
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
    ts1 = np.array([[1,2], [3,4], [4,5], [9,8]])
    ts2 = np.array([[1,2], [3,4], [7,6], [8,7], [9,8]])
    
    dist, path = dtw_distance_multivariate(ts1, ts2)
    print("Multivariate DTW Distance:", dist)
    print("Alignment Path:", path)
