# plot_alignment.py
import matplotlib.pyplot as plt
import numpy as np
from dtw_univariate import dtw_distance
from experiment_cases import (
    generate_base_series,
    scale_change,
    offset_change,
    time_shift
)

def plot_dtw_alignment(ts1, ts2, path, title="DTW Alignment"):
    """
    Visualize DTW alignment between two time series

    Parameters
    ----------
    ts1 : array-like
        Base time series
    ts2 : array-like
        Modified time series
    path : list of tuple
        DTW alignment path
    title : str
        Plot title
    """
    ts1 = np.array(ts1)
    ts2 = np.array(ts2)

    plt.figure(figsize=(12, 5))
    plt.plot(ts1, label="Base Series", linewidth=2)
    plt.plot(ts2, label="Modified Series", linestyle="--")

    # Draw DTW alignment lines
    for (i, j) in path:
        plt.plot([i, j], [ts1[i], ts2[j]], color="gray", alpha=0.3)

    plt.title(title)
    plt.xlabel("Time Index")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # ==================================================
    # Generate common synthetic data
    # ==================================================
    base = generate_base_series(N=200)

    case_scale  = scale_change(base, alpha=3.0)
    case_offset = offset_change(base, beta=5.0)
    case_shift  = time_shift(base, tau=20)

    # ==================================================
    # DTW alignment
    # ==================================================
    _, path_scale  = dtw_distance(base, case_scale)
    _, path_offset = dtw_distance(base, case_offset)
    _, path_shift  = dtw_distance(base, case_shift)

    # ==================================================
    # Visualization
    # ==================================================
    plot_dtw_alignment(base, case_scale, path_scale,
                       title="DTW Alignment – Scale Change (α = 3.0)")

    plot_dtw_alignment(base, case_offset, path_offset,
                       title="DTW Alignment – Offset Change (β = 5.0)")

    plot_dtw_alignment(base, case_shift, path_shift,
                       title="DTW Alignment – Time Shift (τ = 20)")
