# image_metrics.py
import numpy as np
from scipy.ndimage import convolve

def calculate_metrics(matrix):
    arr = np.array(matrix, dtype=np.float64)
    if arr.size == 0:
        return None
    # 1. Độ sáng trung bình
    mean_brightness = np.mean(arr)
    # 2. Độ tương phản (RMS Contrast)
    contrast = np.std(arr)
    # 3. Entropy
    arr_norm = np.clip(arr, 0, 255).astype(np.uint8)
    hist, _ = np.histogram(arr_norm, bins=256, range=(0, 256))
    hist = hist[hist > 0]
    prob = hist / hist.sum()
    entropy = -np.sum(prob * np.log2(prob + 1e-10)) 
    # 4. Độ sắc nét (Laplacian variance)
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    laplacian = convolve(arr, kernel, mode='reflect')
    sharpness = np.var(laplacian)
    return {
        "mean_brightness": round(mean_brightness, 3),
        "contrast": round(contrast, 3),
        "entropy": round(entropy, 3),
        "sharpness": round(sharpness, 3)
    }