# image_enhancement.py
import numpy as np
from PIL import Image

def negative_image(img):
    gray = img.convert("L")
    arr= np.array(gray)
    return Image.fromarray(255 - arr)
def log_transform(img, c=30.0, base=np.e):
    gray= img.convert("L")
    arr = np.array(gray, dtype=np.float64) / 255.0
    transformed = c * np.log(1 + arr) / np.log(base)
    result = np.clip(transformed, 0, 1) * 255
    return Image.fromarray(result.astype("uint8"))
def inverse_log_transform(img, c=30.0, base=np.e):
    gray = img.convert("L")
    arr = np.array(gray, dtype=np.float64) / 255.0
    restored = (base ** (arr / c)) - 1
    result= np.clip(restored, 0, 1) * 255
    return Image.fromarray(result.astype("uint8"))
def gamma_transform(img, c=1.0, gamma=1.0):
    gray = img.convert("L")
    arr = np.array(gray, dtype=np.float64)/ 255.0
    transformed = c * (arr ** gamma)
    result = np.clip(transformed, 0, 1) * 255
    return Image.fromarray(result.astype("uint8"))