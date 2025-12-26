# experiment_cases.py
import numpy as np
from scipy.interpolate import interp1d

def generate_base_series(length=50, seed=42):
    """
    產生基準序列 (單維)
    :param length: 序列長度
    :param seed: 隨機種子
    :return: numpy array
    """
    np.random.seed(seed)
    t = np.linspace(0, 4*np.pi, length)
    base = np.sin(t) + 0.1 * np.random.randn(length)
    return base

def time_shift_series(series, shift=5):
    """
    產生時間偏移序列
    :param series: 原序列 numpy array
    :param shift: 向右偏移幾個時間點 (正值往右)
    :return: numpy array
    """
    n = len(series)
    shifted = np.zeros_like(series)
    if shift >= 0:
        shifted[shift:] = series[:n-shift]
        shifted[:shift] = series[0]  # 用第一個值填補
    else:
        shift = abs(shift)
        shifted[:n-shift] = series[shift:]
        shifted[n-shift:] = series[-1]  # 用最後一個值填補
    return shifted

def time_stretch_series(series, factor=1.5):
    """
    產生時間拉伸/壓縮序列
    :param series: 原序列 numpy array
    :param factor: 拉伸因子 >1 拉長, <1 壓縮
    :return: numpy array
    """
    n = len(series)
    t_original = np.linspace(0, 1, n)
    t_new = np.linspace(0, 1, int(n*factor))
    f = interp1d(t_original, series, kind='linear')
    stretched = f(t_new)
    return stretched

if __name__ == "__main__":
    # 範例
    base = generate_base_series(length=20)
    shifted = time_shift_series(base, shift=3)
    stretched = time_stretch_series(base, factor=1.5)

    print("Base Series:", base)
    print("Time Shifted Series:", shifted)
    print("Time Stretched Series:", stretched)
