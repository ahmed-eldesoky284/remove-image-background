import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("إزالة الخلفية من الصور")

uploaded_file = st.file_uploader("اختر صورة لتحميلها", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # قراءة الصورة التي تم تحميلها
    image = Image.open(uploaded_file)

    # عرض الصورة الأصلية
    st.image(image, caption="الصورة الأصلية", use_column_width=True)

    # إزالة الخلفية من الصورة
    output_image = remove(image)

    # عرض الصورة الناتجة
    st.image(output_image, caption="الصورة بدون خلفية", use_column_width=True)

    # حفظ الصورة الناتجة
    buffer = io.BytesIO()
    output_image.save(buffer, format="PNG")
    buffer.seek(0)

    # توفير خيار لتحميل الصورة الناتجة
    st.download_button(
        label="تحميل الصورة بدون خلفية",
        data=buffer,
        file_name="image_no_bg.png",
        mime="image/png"
    )
