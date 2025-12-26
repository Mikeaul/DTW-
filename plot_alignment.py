# plot_alignment.py
import matplotlib.pyplot as plt
import numpy as np

def plot_dtw_alignment(ts1, ts2, path, title="DTW Alignment"):
    """
    繪製兩條時間序列與 DTW 對齊路徑
    :param ts1: numpy array 或 list, 序列1
    :param ts2: numpy array 或 list, 序列2
    :param path: DTW alignment path, list of tuples [(i,j), ...]
    :param title: 圖片標題
    """
    ts1 = np.array(ts1)
    ts2 = np.array(ts2)

    plt.figure(figsize=(10, 5))
    plt.plot(ts1, label="Series 1", marker='o')
    plt.plot(ts2, label="Series 2", marker='x')

    # 畫對齊路徑
    for (i, j) in path:
        plt.plot([i, j], [ts1[i], ts2[j]], color='gray', alpha=0.5)

    plt.title(title)
    plt.xlabel("Time Index")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 範例測試
    ts1 = [1, 3, 4, 9]
    ts2 = [1, 3, 7, 8, 9]

    # 範例對齊路徑 (假設從 dtw_distance 回傳)
    path = [(0,0), (1,1), (2,2), (2,3), (3,4)]

    plot_dtw_alignment(ts1, ts2, path, title="Example DTW Alignment")
