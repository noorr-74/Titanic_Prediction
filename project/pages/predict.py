import streamlit as st
import numpy as np
import joblib

# ================= PAGE =================

st.set_page_config(
    page_title="Titanic Prediction",
    layout="centered"
)

st.title("🎯 Titanic Survival Prediction")

st.write("Enter passenger information below:")

# ================= MODEL SELECTION =================

# ================= ADVANCED OPTIONS =================

advanced_mode = st.checkbox(
    "Advanced User (Choose ML Model)"
)

# default model
model_choice = "Random Forest"

# show model selection only if checkbox enabled
if advanced_mode:

    model_choice = st.selectbox(
        "Choose Machine Learning Model",
        [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "SVM"
        ]
    )

# ================= LOAD MODEL =================

if model_choice == "Logistic Regression":

    model = joblib.load("logistic.pkl")

elif model_choice == "Decision Tree":

    model = joblib.load("decision_tree.pkl")

elif model_choice == "Random Forest":

    model = joblib.load("randomforest.pkl")

else:

    model = joblib.load("svm.pkl")

    # load scaler for svm
    scaler = joblib.load("scaler.pkl")

# ================= INPUTS =================

col1, col2 = st.columns(2)

with col1:

    pclass = st.selectbox(
        "Passenger Class",
        [1, 2, 3]
    )

    if pclass == 3:

        fare_category = st.selectbox(
        "Fare Range",
        ["3 - 10"]
    )

        fare = 7

    elif pclass == 2:

        fare_category = st.selectbox(
        "Fare Range",
        ["11 - 30"]
    )

        fare = 20

    else:

        fare_category = st.selectbox(
        "Fare Range",
        ["31 - 600"]
    )

        fare = 50




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

# ================= SVM SCALING =================

if model_choice == "SVM":

    input_data = scaler.transform(input_data)

# ================= PREDICTION =================

if st.button("Predict"):

    prediction = model.predict(input_data)

    st.subheader(f"Model Used: {model_choice}")

    if prediction[0] == 1:

        st.success("✅ Passenger Survived")

    else:

        st.error("❌ Passenger Did Not Survive")