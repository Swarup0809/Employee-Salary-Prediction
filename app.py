import streamlit as st
import joblib
import numpy as np
from datetime import datetime

# Set page config for better aesthetics
st.set_page_config(
    page_title="🔮 Employee Salary Predictor",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar with company branding and info
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.title("💼 Salary Predictor")
    st.markdown("Predict company employee salaries using machine learning.")
    st.markdown("---")
    st.caption(f"Date: {datetime.now().strftime('%B %d, %Y')}")

# Main header
st.title("🔮 Employee Salary Prediction App")

st.write("""
Welcome to the next-generation salary predictor! Enter an employee's details and let AI estimate their likely salary instantly.
""")

st.markdown("### 📝 Employee Details")

# Input fields in columns for modern look
col1, col2 = st.columns(2)
with col1:
    years = st.number_input("Years at Company", min_value=0, value=1, step=1, help="Number of years the employee has worked in the company")
with col2:
    jobrate = st.slider("Job Performance Rating", min_value=0.0, max_value=5.0, value=3.5, step=0.5, help="Rate the employee's performance (0–5)")

# Load model (try/except block for better UX)
@st.cache_resource
def load_model():
    return joblib.load("linearmodel.pkl")

try:
    model = load_model()
except Exception:
    st.error("🚨 Model file not found. Please upload 'linearmodel.pkl' to the app directory.")
    st.stop()

X = [[years, jobrate]]

# Show status message or prediction result
if st.button("🎯 Predict Salary"):
    with st.spinner("Calculating prediction..."):
        prediction = model.predict(X)[0]
        st.success(f"💰 Estimated Salary: **{prediction:,.2f}**/-", icon="💸")
        st.balloons()
        st.markdown("### 🎉 Prediction Details")
        st.write(f"With **{years}** years at the company and a job rating of **{jobrate}**, the predicted salary is shown above.")
        st.info("Note: This estimate is based on historical company data. Individual salaries may vary.", icon="ℹ️")
else:
    st.info("Fill in the details and click **Predict Salary** to get your result!", icon="🧑‍💻")

# Optional: Add some FAQs or company tips
with st.expander("🚀 How does this work?"):
    st.write("This app uses a machine learning model trained on past employee data to make salary predictions. Simply enter employee details and click the button!")

with st.expander("🤔 Improving Your Accuracy"):
    st.write("""
- Use recent data for training the model.
- Include additional features like education, role, or department if possible.
- Regularly update the model as your company grows.
""")
