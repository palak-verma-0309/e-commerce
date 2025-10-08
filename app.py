import streamlit as st
import pandas as pd
import joblib

st.title("E-Commerce Sales & Profit Prediction App")

model = joblib.load("model.joblib")

st.header("Enter Customer & Order Details")

gender = st.selectbox("Gender", ["Male", "Female"])
device = st.selectbox("Device Type", ["Mobile", "Desktop", "Tablet"])
login = st.selectbox("Login Type", ["Guest", "Registered"])
category = st.selectbox("Product Category", ["Electronics", "Clothing", "Accessories", "Home", "Other"])
priority = st.selectbox("Order Priority", ["Low", "Medium", "High", "Critical"])
payment = st.selectbox("Payment Method", ["COD", "Credit Card", "Debit Card", "UPI", "Wallet"])

quantity = st.slider("Quantity", 1, 10, 2)
discount = st.number_input("Discount (%)", min_value=0.0, max_value=0.5, step=0.05)
shipping = st.number_input("Shipping Cost", min_value=0.0, max_value=20.0, step=0.5)
aging = st.number_input("Aging (Days)", min_value=1.0, max_value=15.0, step=1.0)

if st.button("Predict Sales & Profit"):
    input_df = pd.DataFrame([{
        "Gender": gender,
        "Device_Type": device,
        "Customer_Login_type": login,
        "Product_Category": category,
        "Order_Priority": priority,
        "Payment_method": payment,
        "Quantity": quantity,
        "Discount": discount,
        "Shipping_Cost": shipping,
        "Aging": aging
    }])
    
    preds = model.predict(input_df)
    sales, profit = preds[0]
    
    st.success(f"Predicted Sales: {sales:.2f}")
    st.success(f"Predicted Profit: {profit:.2f}")
