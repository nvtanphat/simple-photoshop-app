from PIL import Image
import numpy as np
import state
import io

# Bài 2a: Chuyển ảnh xám
def convert_to_gray(img=None):
    target = img if img is not None else state.current_image
    return target.convert("L")
# Bài 3: Nhị phân hóa
def convert_to_binary(threshold=128):
    gray= state.current_image.convert("L")
    arr = np.array(gray)
    binary = (arr > threshold) * 255
    return Image.fromarray(binary.astype("uint8"))
# Bài 4: Tách kênh Red
def extract_red_channel():
    img= state.original_image.convert("RGB")
    r, g,b= img.split()
    zero = Image.new("L", img.size, 0)
    return Image.merge("RGB", (r, zero, zero))
# Bài 5: Tách kênh Alpha
def extract_alpha_channel():
    img = state.original_image
    if img.mode != "RGBA":
        return None
    r, g, b, a = img.split()
    return a
# Bài 1: Lưu ảnh
def get_bytes(format="PNG"):
    buf = io.BytesIO()
    state.current_image.save(buf, format=format)
    return buf.getvalue()
