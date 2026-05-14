import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Titanic Dashboard",
    layout="wide"
)

# ================= LOAD DATA =================

path = r"C:\Users\youse\Desktop\python for vs\project\Titanic_train.csv.csv"

train = pd.read_csv(path)

scores = joblib.load(r"C:\Users\youse\Desktop\python for vs\project\acc.pkl")
# ================= BACKGROUND =================

page_bg = """
<style>

[data-testid="stAppViewContainer"]{
background:
linear-gradient(
135deg,
#0f172a,
#1e293b,
#334155
);
color:white;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

[data-testid="stSidebar"]{
background-color:#111827;
}

h1,h2,h3,h4,h5,h6,p,label,div{
color:white;
}

img{
max-width:100%;
height:auto;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ================= TITLE =================

st.title("📊 Titanic Dashboard")

st.write("Machine Learning Models Analysis")

st.markdown("---")

# ================= SIDEBAR =================

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose Section",
    [
        "Overview of Titanic",
        "Model Accuracy",
        "Age Distribution",
        "Survival Rate",
        "Feature Analysis",
        "Missing Values",
        "Dataset Statistics"
    ]
)

# ================= METRICS =================

best_model = max(scores, key=scores.get)

best_score = scores[best_model]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Models Used",
    "4"
)

col2.metric(
    "Best Model",
    best_model
)

col3.metric(
    "Best Accuracy",
    f"{best_score*100:.2f}%"
)

st.markdown("---")

# ================= FUNCTIONS =================

def plot_age_distribution(df):

    fig, ax = plt.subplots(figsize=(10,5))

    ax.hist(
        df["Age"].dropna(),
        bins=20
    )

    ax.set_title("Age Distribution")

    ax.set_xlabel("Age")

    ax.set_ylabel("Frequency")

    st.pyplot(fig, use_container_width=True)


def build_survival_rate_chart(df):

    fig, ax = plt.subplots(figsize=(7,5))

    survival_counts = df["Survived"].value_counts()

    labels = ["Dead", "Survived"]

    ax.pie(
        survival_counts,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax.set_title("Survival Rate")

    st.pyplot(fig, use_container_width=True)


def build_bar_chart(feature):

    fig, ax = plt.subplots(figsize=(10,5))

    sns.countplot(
        x=feature,
        hue="Survived",
        data=train,
        ax=ax
    )

    ax.set_title(f"{feature} vs Survival")

    st.pyplot(fig, use_container_width=True)

# ================= OVERVIEW =================

if page == "Overview of Titanic":

    st.subheader("🚢 Overview of the Titanic Dataset")

    st.write("""
    The Titanic dataset is one of the most famous datasets in Machine Learning.
    
    The goal is to predict whether a passenger survived or not based on:
    
    - Gender
    - Passenger Class
    - Age
    - Family Size
    - Ticket Information
    
    This dashboard analyzes:
    
    1. Machine Learning Models Accuracy
    2. Passenger Age Distribution
    3. Survival Rate
    4. Feature Impact on Survival
    """)

    st.dataframe(train.head())

# ================= MODEL ACCURACY =================

elif page == "Model Accuracy":

    st.subheader("📈 Model Accuracy Comparison")

    df_scores = pd.DataFrame({

        "Model": list(scores.keys()),

        "Accuracy": [score * 100 for score in scores.values()]

    })

    df_scores = df_scores.sort_values(
        by="Accuracy",
        ascending=False
    )

    df_scores.index = range(1, len(df_scores) + 1)

    col1, col2 = st.columns(2)

    with col1:

        fig, ax = plt.subplots(figsize=(8,5))

        ax.bar(
            df_scores["Model"],
            df_scores["Accuracy"]
        )

        ax.set_xlabel("Models")

        ax.set_ylabel("Accuracy %")

        ax.set_title("Machine Learning Models Accuracy")

        st.pyplot(fig, use_container_width=True)

    with col2:

        st.subheader("📋 Accuracy Ranking")

        st.dataframe(df_scores)

# ================= AGE DISTRIBUTION =================

elif page == "Age Distribution":

    st.subheader("👥 Age Distribution")

    plot_age_distribution(train)

# ================= SURVIVAL RATE =================

elif page == "Survival Rate":

    st.subheader("🚢 Survival Rate")

    build_survival_rate_chart(train)

# ================= FEATURE ANALYSIS =================

elif page == "Feature Analysis":

    st.subheader("📊 Categorical Feature Analysis")

    feature = st.selectbox(
        "Choose Feature",
        ["Sex", "Pclass", "Embarked"]
    )

    build_bar_chart(feature)

# ================= MISSING VALUES =================

elif page == "Missing Values":

    st.subheader("❌ Missing Values")

    missing_values = train.isnull().sum()

    missing_values = missing_values[missing_values > 0]

    st.dataframe(missing_values)

# ================= DATASET STATISTICS =================

elif page == "Dataset Statistics":

    st.subheader("📈 Dataset Statistics")

    st.dataframe(train.describe())

# ================= FOOTER =================

st.markdown("---")

st.subheader("🚢 Titanic Insights")

st.write("""
- Random Forest usually performs best on Titanic dataset.
- Female passengers had higher survival rates.
- Passenger class strongly affected survival.
- Family size also impacts prediction.
""")

st.success("Dashboard Loaded Successfully")