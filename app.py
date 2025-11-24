import streamlit as st
from ui_components import render_sidebar, render_display

#Thiết lập gaio dien Streamlit
#Đặt tiêu đề trang
st.set_page_config(page_title="Ứng dụng xử lý ảnh")
#Chèn mà CSS tùy chỉnh vào trang
#Có thể ẩn menu chính, chân trang và tiêu đề
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
selected_action, threshold = render_sidebar() #Giao diện thanh bên
render_display(selected_action, threshold) #Hiển thị
