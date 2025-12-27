# experiment_cases.py
import numpy as np

# ======================================================
# Synthetic Time Series - Common Experimental Cases
# ======================================================

def generate_base_series(N=200):
    """
    Generate base synthetic time series
    x(t) = sin(t), t in [0, 2π]

    Parameters
    ----------
    N : int
        Length of time series

    Returns
    -------
    np.ndarray
        Base time series of shape (N,)
    """
    t = np.linspace(0, 2 * np.pi, N)
    x = np.sin(t)
    return x


def scale_change(series, alpha=3.0):
    """
    Case 1: Scale change
    y = alpha * x

    Parameters
    ----------
    series : np.ndarray
        Base time series
    alpha : float
        Scaling factor

    Returns
    -------
    np.ndarray
        Scaled time series
    """
    return alpha * series


def offset_change(series, beta=5.0):
    """
    Case 2: Offset change
    y = x + beta

    Parameters
    ----------
    series : np.ndarray
        Base time series
    beta : float
        Offset value

    Returns
    -------
    np.ndarray
        Offset time series
    """
    return series + beta


def time_shift(series, tau=20):
    """
    Case 3: Time shift (circular shift)
    y = roll(x, tau)

    Parameters
    ----------
    series : np.ndarray
        Base time series
    tau : int
        Shift amount (number of samples)

    Returns
    -------
    np.ndarray
        Time-shifted time series
    """
    return np.roll(series, tau)


# ======================================================
# Example usage
# ======================================================
if __name__ == "__main__":
    base = generate_base_series()

    case_scale = scale_change(base)
    case_offset = offset_change(base)
    case_shift = time_shift(base)

    print("Base series length:", len(base))
    print("Scale case example:", case_scale[:5])
    print("Offset case example:", case_offset[:5])
    print("Time shift case example:", case_shift[:5])

