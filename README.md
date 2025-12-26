# Time Series Similarity Comparison with Dynamic Time Warping (DTW)

## 1. 專案檔案

- `dtw_univariate.py`  
  單變量 DTW 實作，輸入兩條一維時間序列，輸出：
  - DTW 距離
  - 對齊（alignment）路徑  

- `dtw_multivariate.py`  
  多維（Multivariate）DTW 實作，每個時間點為向量，
  使用 Euclidean distance 作為局部距離計算方式。

- `similarity_compare.py`  
  與 Euclidean Distance 進行對照實驗，
  比較「時間對齊前後」距離差異。

- `experiment_cases.py`  
  共用測試資料產生模組，產生：
  - base series
  - time shift case
  - time stretching case  

- `plot_alignment.py`  
  視覺化時間序列與 DTW 對齊結果（alignment path），
  用於簡報與報告展示。

- `README.md`  
  本說明文件。

（共用實驗設定與其他方法請參考 Repo 根目錄之說明文件。）

---

## 2. 環境需求

- Python 3.10+（建議 3.11）

### 必要套件
- numpy
- matplotlib

### （選用）
- scipy（距離計算）
- fastdtw（加速版本對照實驗）

---

## 3. 環境建議安裝方式（conda）

```bash
conda create -n ts-sim python=3.11 -y
conda activate ts-sim
conda install numpy matplotlib scipy -y

