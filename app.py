import streamlit as st
import joblib

st.title("Fruit Type Classification")

model = joblib.load('decision_tree_model.joblib')

Color = st.number_input("Color", min_value=0, max_value=2, value=1)
Weight = st.number_input("Weight", min_value=100, max_value=175, value=110)
Texture = st.number_input("Texture", min_value=0, max_value=1, value=1)
Size = st.number_input("Size", min_value=5.0, max_value=8.0, value=5.5)

sample = [[Color, Weight, Texture, Size]]

fruit_map = {
    0: "Apple",
    1: "Banana",
    2: "Orange",
    3: "Mango"
}

if st.button("Predict"):
    prediction = model.predict(sample)[0]
    fruit_name = fruit_map[prediction]
    st.success(f"Predicted fruit is {fruit_name}")
