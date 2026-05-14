import streamlit as st
import numpy as np
import joblib

# ================= LOAD MODEL =================

model = joblib.load("model.pkl")

# ================= PAGE =================

st.set_page_config(page_title="Titanic Prediction", layout="centered")

st.title("🚢 Titanic Survival Prediction")

st.write("Enter passenger information below:")

# ================= INPUTS =================

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    
    sex = st.selectbox(
        "Sex",
        ["male", "female"]
    )

    if sex == "male":

        title = st.selectbox(
        "Title",
        ["Mr", "Other"]
    )

    else:

        title = st.selectbox(
        "Title",
        ["Miss", "Mrs", "Other"]
    )

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=100,
        value=25
    )

    fare = st.number_input(
        "Fare",
        min_value=0.0,
        max_value=600.0,
        value=50.0
    )

with col2:

    sibsp = st.number_input(
        "Siblings / Spouses",
        min_value=0,
        max_value=10,
        value=0
    )

    parch = st.number_input(
        "Parents / Children",
        min_value=0,
        max_value=10,
        value=0
    )

    embarked = st.selectbox(
        "Embarked",
        ["S", "C", "Q"]
    )



# ================= FEATURE ENGINEERING =================

# sex mapping
sex_mapping = {
    "male": 0,
    "female": 1
}

sex = sex_mapping[sex]

# embarked mapping
embarked_mapping = {
    "S": 0,
    "C": 1,
    "Q": 2
}

embarked = embarked_mapping[embarked]

# title mapping
title_mapping = {
    "Mr": 0,
    "Miss": 1,
    "Mrs": 2,
    "Other": 3
}

title = title_mapping[title]

# family size
family_size = sibsp + parch + 1

# alone feature
alone = 1 if family_size == 1 else 0

# ================= INPUT ARRAY =================

input_data = np.array([[
    pclass,
    sex,
    age,
    sibsp,
    parch,
    fare,
    embarked,
    title,
    family_size,
    alone
]])

# ================= PREDICTION =================

if st.button("Predict"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Passenger Survived")
    else:
        st.error("❌ Passenger Did Not Survive")