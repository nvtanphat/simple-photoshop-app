
import streamlit as st
import numpy as np
import state
import image_utils
from image_metrics import calculate_metrics
from image_enhancement import negative_image, log_transform, inverse_log_transform, gamma_transform
from PIL import Image

#Khởi tạo ma trận M ở bài 2
# Ma trận M
M = np.array([
    [1,1,1,1,1,1,1,1,1,1],[1,2,2,3,1,1,1,7,2,1],[1,2,3,2,1,1,5,3,6,1],
    [1,3,2,2,1,1,0,4,1,1],[1,1,1,1,1,1,1,1,1,1],[1,0,0,0,1,1,1,1,1,1],
    [1,0,7,7,1,1,1,1,1,1],[1,0,7,7,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1]
])
#Hàm thiển thị thanh phần menu
def render_sidebar():
    st.sidebar.title("Menu điều khiển")
    uploaded_file = st.sidebar.file_uploader("Tải ảnh lên", type=["png","jpg","jpeg","bmp","gif","tiff"])
    if uploaded_file:
        state.original_image = Image.open(uploaded_file)
        state.current_image = state.original_image.copy()
        st.sidebar.success(f"Đã tải: {uploaded_file.name}")
    #Danh sách các chức năng
    actions = [
        "Xem ảnh gốc","Bài 1.2.1: Ảnh xám","Bài 1.2.2: Ma trận xám","Bài 1.3: Nhị phân hóa",
        "Bài 1.4: Kênh Red","Bài 1.5: Kênh Alpha","Bài 2: Tính 4 chỉ số ảnh",
        "Bài 3.1: Ảnh âm bản","Bài 3.2: Biến đổi Logarit","Bài 3.3: Logarit ngược","Bài 3.4: Biến đổi Gamma"
    ]
    selected_action = st.sidebar.radio("Chọn chức năng:", actions)
    #Hiển thị thêm thanh trượt cho bài 1.3
    threshold = st.sidebar.slider("Ngưỡng nhị phân",0,255,128,key="thresh") if selected_action == "Bài 1.3: Nhị phân hóa" else None
    return selected_action, threshold
#Hàm hiển thị kết quả dựa trên lựa chọn
def render_display(selected_action, threshold):
    st.header("Kết quả xử lý")
    if not state.original_image and selected_action not in ["Bài 2: Tính 4 chỉ số ảnh"]:
        st.info("Vui lòng upload ảnh!")
        return
    if selected_action == "Xem ảnh gốc":
        state.current_image = state.original_image
    elif selected_action == "Bài 1.2.1: Ảnh xám":
        state.current_image = image_utils.convert_to_gray()
    elif selected_action == "Bài 1.2.2: Ma trận xám":
        arr = np.array(image_utils.convert_to_gray())
        st.dataframe(arr[:10, :10] if arr.shape[0] > 10 else arr)
        return
    elif selected_action == "Bài 1.3: Nhị phân hóa":
        state.current_image = image_utils.convert_to_binary(threshold)
    elif selected_action == "Bài 1.4: Kênh Red":
        state.current_image = image_utils.extract_red_channel()
    elif selected_action == "Bài 1.5: Kênh Alpha":
        alpha = image_utils.extract_alpha_channel()
        if not alpha: st.warning("Không có kênh Alpha!"); return
        state.current_image = alpha
    # Bài tập 2
    elif selected_action == "Bài 2: Tính 4 chỉ số ảnh":
        st.markdown("## Phân tích chỉ số ảnh")
        st.dataframe(M); st.success(f"M: {calculate_metrics(M)}")
        A,B,C = M[1:4,1:4], M[6:9,1:4], M[1:4,5:8]
        c1,c2,c3 = st.columns(3)
        with c1: st.subheader("A"); st.dataframe(A); st.info(str(calculate_metrics(A)))
        with c2: st.subheader("B"); st.dataframe(B); st.info(str(calculate_metrics(B)))
        with c3: st.subheader("C"); st.dataframe(C); st.info(str(calculate_metrics(C)))
        if state.original_image:
            gray = state.original_image.convert("L")
            st.image(gray, "Ảnh xám thực tế")
            st.success(f"Ảnh thực: {calculate_metrics(np.array(gray))}")
        return
    # Bài tập 3
    elif selected_action == "Bài 3.1: Ảnh âm bản":
        st.subheader("Ảnh âm bản")
        gray = state.original_image.convert("L")
        neg = negative_image(state.original_image)
        state.current_image = neg
        c1, c2 = st.columns(2)
        with c1: st.image(gray, "Gốc")
        with c2: st.image(neg, "Âm bản")
    elif selected_action == "Bài 3.2: Biến đổi Logarit":
        st.subheader("Làm sáng ảnh bằng Logarit")
        c = st.slider("c", 0.1, 5.0, 1.0)
        base = np.e if st.radio("Cơ số",["e", "10"]) == "e" else 10
        enhanced = log_transform(state.original_image, c, base)
        state.current_image = enhanced
        c1,c2 = st.columns(2)
        with c1: st.image(state.original_image.convert("L"), "Ảnh tối")
        with c2: st.image(enhanced, f"Logarit c={c}")
    elif selected_action == "Bài 3.3: Logarit ngược":
        st.subheader("Khôi phục ảnh chói bằng Log ngược")
        c = st.slider("c", 0.1, 5.0, 1.0, key="c_inv")
        base = np.e if st.radio("Cơ số",["e", "10"], key="base_inv") == "e" else 10
        restored = inverse_log_transform(state.current_image, c, base)
        state.current_image = restored
        c1,c2 = st.columns(2)
        with c1: st.image(state.original_image.convert("L"), "Ảnh chói")
        with c2: st.image(restored, "Đã khôi phục")
    elif selected_action == "Bài 3.4: Biến đổi Gamma":
        st.subheader("Hiệu chỉnh Gamma")
        c = st.slider("c", 0.1, 3.0, 1.0)
        gamma = st.slider("γ", 0.1, 5.0, 1.0)
        gamma_img = gamma_transform(state.original_image, c, gamma)
        state.current_image = gamma_img
        c1,c2 = st.columns(2)
        with c1: st.image(state.original_image.convert("L"), "Gốc")
        with c2: st.image(gamma_img, f"Gamma γ={gamma}")
    # Hiển thị + tải về
    if selected_action not in ["Bài 2: Tính 4 chỉ số ảnh", "Bài 1.2.2: Ma trận xám"]:
        left, center, right = st.columns([1, 2, 1])
        with center:
            st.image(state.current_image, "Kết quả", use_column_width=True)
            fmt = st.selectbox("Lưu định dạng",["png","jpeg","bmp"], key="save")
            buf = image_utils.get_bytes("PNG" if fmt=="png" else fmt.upper())
            st.download_button("Tải ảnh", data=buf, file_name=f"result.{fmt}", mime=f"image/{fmt}")