# Ứng dụng Xử lý Ảnh (Image Processing App)

Đây là một ứng dụng web đơn giản được xây dựng bằng **Streamlit**, cho phép người dùng tải lên hình ảnh và thực hiện các thao tác xử lý ảnh cơ bản cũng như tính toán các chỉ số của ảnh.

## Tính năng chính

Ứng dụng cung cấp các chức năng sau:

### 1. Tăng cường và Biến đổi ảnh (Image Enhancement)
*   **Ảnh âm bản (Negative Image):** Chuyển đổi ảnh sang dạng âm bản.
*   **Biến đổi Log (Log Transformation):** Tăng cường độ tương phản cho vùng tối của ảnh.
*   **Biến đổi Log nghịch đảo (Inverse Log Transformation):** Tăng cường độ tương phản cho vùng sáng.
*   **Biến đổi Gamma (Gamma Correction):** Điều chỉnh độ sáng của ảnh phi tuyến tính.

### 2. Tính toán chỉ số ảnh (Image Metrics)
Tính toán các thông số kỹ thuật của ảnh:
*   **Độ sáng trung bình (Mean Brightness)**
*   **Độ tương phản (Contrast - RMS)**
*   **Entropy:** Đo lượng thông tin trong ảnh.
*   **Độ sắc nét (Sharpness):** Sử dụng phương sai Laplacian.

## Cài đặt

Để chạy ứng dụng, bạn cần cài đặt Python và các thư viện cần thiết.

1.  **Yêu cầu hệ thống:**
    *   Python 3.x

2.  **Cài đặt thư viện:**
    Mở terminal và chạy lệnh sau để cài đặt các gói phụ thuộc:
    ```bash
    pip install streamlit numpy pillow scipy
    ```

## Hướng dẫn sử dụng

1.  Mở terminal tại thư mục chứa dự án.
2.  Chạy ứng dụng bằng lệnh:
    ```bash
    streamlit run app.py
    ```
3.  Trình duyệt sẽ tự động mở ứng dụng (thường tại địa chỉ `http://localhost:8501`).
4.  Tải lên một hình ảnh và chọn các tác vụ từ thanh bên (Sidebar) để xem kết quả.

## Cấu trúc dự án

*   `app.py`: File chính để chạy ứng dụng Streamlit.
*   `ui_components.py`: Chứa các thành phần giao diện người dùng (Sidebar, Display).
*   `image_enhancement.py`: Chứa các hàm xử lý biến đổi ảnh.
*   `image_metrics.py`: Chứa các hàm tính toán chỉ số ảnh.
*   `image_utils.py`: Các hàm tiện ích hỗ trợ xử lý ảnh.
*   `state.py`: Quản lý trạng thái của ứng dụng.


