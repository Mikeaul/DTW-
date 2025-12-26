# plot_alignment.py
import matplotlib.pyplot as plt
import numpy as np
from dtw_univariate import dtw_distance            # 單維 DTW
from experiment_cases import generate_base_series, time_shift_series, time_stretch_series

def plot_dtw_alignment(ts1, ts2, path, title="DTW Alignment"):
    """
    繪製兩條時間序列與 DTW 對齊路徑
    :param ts1: list 或 numpy array, 序列1
    :param ts2: list 或 numpy array, 序列2
    :param path: DTW alignment path, list of tuples [(i,j), ...]
    :param title: 圖片標題
    """
    ts1 = np.array(ts1)
    ts2 = np.array(ts2)

    plt.figure(figsize=(10, 5))
    plt.plot(ts1, label="Series 1 (Base)", marker='o')
    plt.plot(ts2, label="Series 2 (Variant)", marker='x')

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
    # 產生實驗案例
    base_series = generate_base_series(length=20)
    shifted_series = time_shift_series(base_series, shift=3)
    stretched_series = time_stretch_series(base_series, factor=1.5)

    # 單維 DTW 計算
    dist_shift, path_shift = dtw_distance(base_series, shifted_series)
    dist_stretch, path_stretch = dtw_distance(base_series, stretched_series)

    # 視覺化
    plot_dtw_alignment(base_series, shifted_series, path_shift, title="Time Shift DTW Alignment")
    plot_dtw_alignment(base_series, stretched_series, path_stretch, title="Time Stretch DTW Alignment")

