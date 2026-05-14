# %%
import pandas as pd
import numpy as np

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# %%
train=pd.read_csv(r"C:\Users\youse\Downloads\Titanic_train.csv.csv")
test=pd.read_csv(r"C:\Users\youse\Downloads\Titanic_test.csv.csv")

# %%
#from google.colab import drive
#drive.mount('/content/drive')

# %%
train.head()

# %% [markdown]
# # Data Dictionary
# - Survived: 0 = No, 1 = Yes
# - pclass: Ticket class 1 = 1st, 2 = 2nd, 3 = 3rd
# - sibsp: # of siblings / spouses aboard the Titanic
# - parch: # of parents / children aboard the Titanic
# - ticket: Ticket number
# - cabin: Cabin number
# - embarked: Port of Embarkation C = Cherbourg, Q = Queenstown, S = Southampton

# %%
#remove the columns which is not needed(Name ,Ticket ,passengerId,cabin)
train.drop(['Ticket', 'PassengerId', 'Cabin'], axis=1, inplace=True)
test.drop(['Ticket', 'PassengerId', 'Cabin'], axis=1, inplace=True)

# %%
train.info()

# %%
train.isnull().sum()

# %%
test.info()

# %%
test.isnull().sum()

# %% [markdown]
# # 🚢 Survival Rate Analysis
# 

# %%


def build_survival_rate_chart(train):

    import matplotlib.pyplot as plt

    survival_counts = train["Survived"].value_counts()

    labels = ["Did Not Survive", "Survived"]

    fig, ax = plt.subplots(figsize=(6,6))

    ax.pie(
        survival_counts,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax.set_title("Survival Rate Analysis")

    return fig
build_survival_rate_chart(train)

plt.show()


# %% [markdown]
# # Bar Chart for categorical Features
# - PClass
# - Sex
# - SibSp (# of siblings and spouse)
# - ParCh (# of parrents and children)
# - Embarked
# - Cabin

# %%
# function to build a bar chart for a specified feature to visualize the distribution of survivors and non-survivors
def build_bar_chart(feature):
    survived = train[train['Survived']==1][feature].value_counts()
    dead = train[train['Survived']==0][feature].value_counts()

    df = pd.DataFrame([survived, dead])
    df.index = ['Survived', 'Dead']
    df.plot(kind='bar', stacked=True,figsize=(10, 5))

# %%
build_bar_chart('Sex')

# %% [markdown]
# # age distribution
# 

# %%
import matplotlib.pyplot as plt

def plot_age_distribution(df):
    plt.figure(figsize=(8,5))
    
    plt.hist(df["Age"].dropna(), bins=20)
    
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    
    plt.show()

plot_age_distribution(train)

# %% [markdown]
# That confirms **Women** more likely survived than **Men**

# %%
build_bar_chart('Pclass')

# %% [markdown]
# The Chart confirms **1st** class more likely survivied than **other classes**
# 
# The Chart confirms **3rd** class more likely dead than **other classes**

# %%
build_bar_chart('SibSp')

# %% [markdown]
# The Chart confirms **a person aboard alone** was more likely to die
# 
# The Chart confirms **a person with 1 or 2 siblings or spouses** was more likely to survive.

# %%
build_bar_chart('Parch')

# %% [markdown]
# The Chart confirms **a person aboard alone** was more likely to die
# 
# The Chart confirms **a person with 1 or 2 family members** was more likely to survive.

# %%
build_bar_chart('Embarked')

# %% [markdown]
# The Chart confirms **a person aboarded from C** slightly more likely survived
# 
# The Chart confirms **a person aboarded from Q** more likely dead
# 
# The Chart confirms **a person aboarded from S** more likely dead
# 

# %% [markdown]
# # Feature Engineering

# %%
from IPython.display import Image
Image(url= "https://static1.squarespace.com/static/5006453fe4b09ef2252ba068/t/5090b249e4b047ba54dfd258/1351660113175/TItanic-Survival-Infographic.jpg?format=1500w")

# %%
train.head()

# %%
#combining train and test datasets for easier data manipulation and extraction title from the name column
train_test_data = [train, test]
for dataset in train_test_data:
    dataset['Title'] = dataset['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)

# %%
#crating new features for family size and whether the passenger is alone or not
for dataset in train_test_data:
    dataset["FamilySize"] = dataset["SibSp"] + dataset["Parch"] + 1
    dataset["Alone"] = (dataset["FamilySize"] == 1).astype(int)

# %%
build_bar_chart('Title')

# %%
build_bar_chart('FamilySize')

# %%
build_bar_chart('Alone')

# %%
#drop Name column after extracting the title from it
drop_cols = ["Name"]
train = train.drop(drop_cols, axis=1)
test = test.drop(drop_cols, axis=1)

# %% [markdown]
# # Missing Value Handling

# %%
#checking for missing values after feature engineering
train.isnull().sum()

# %%
test.isnull().sum()

# %%
# fill missing age with median age for each title (Mr, Mrs, Miss, Others)
train["Age"] = train["Age"].fillna(train.groupby("Title")["Age"].transform("median"))
test["Age"] = test["Age"].fillna(test.groupby("Title")["Age"].transform("median"))

#fill missing age if it still exists with fallback median age in test dataset
test["Age"] = test["Age"].fillna(train["Age"].median())

# %%
# fill missing embarked with the most common value
train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])
test['Embarked'] = test['Embarked'].fillna(test['Embarked'].mode()[0])

# %%
#fill missing fare with median fare for each Pclass
test["Fare"] = test["Fare"].fillna(test.groupby("Pclass")["Fare"].transform("median"))

# %%
#checking for missing values after Handling missing values
train.isnull().sum()

# %%
test.isnull().sum()

# %% [markdown]
# # Checking for Outliers in numeric Features

# %%
# function to create a box plot that displays outliers
def plot_boxplot_with_outliers(feature, data):
    plt.figure(figsize=(12, 6))
    sns.boxplot(y=feature, data=data, palette='Set2',
                fliersize=8, flierprops=dict(marker='o', markerfacecolor='red', markersize=8, alpha=0.7))
    plt.title(f'Box Plot of {feature} (Outliers Highlighted in Red)', fontsize=14, fontweight='bold')
    plt.ylabel(feature, fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()

# %% [markdown]
# # Map dictionary
# - 0--> MR
# - 1--> Miss
# - 2--> Mrs
# - 3--> Other

# %%
title_mapping = {
    "Mr": 0,
    "Miss": 1,
    "Mrs": 2,
    "Master": 3,
    "Dr": 3,
    "Jonkheer": 3,
    "Rev": 3,
    "Col": 3,
    "Major": 3,
    "Mlle": 3,
    "Countess": 3,
    "Ms": 3,
    "Sir": 3,
    "Capt": 3,
    "Mme": 3,
    "Lady": 3,
    "Don": 3,
    "Dona": 3
}
train['Title'] = train['Title'].map(title_mapping)
test['Title'] = test['Title'].map(title_mapping)

# %% [markdown]
# # Map dictionary
# - male-->0
# - female-->1

# %%
sex_mapping={"male":0,"female":1}
train['Sex'] = train['Sex'].map(sex_mapping)
test['Sex'] = test['Sex'].map(sex_mapping)

# %% [markdown]
# # Map dictionary
# - C-->Cherbourg-->1
# - Q-->Queenstown-->2
# - S-->Southampton-->0

# %%
embarked_mapping={"S":0,"C":1,"Q":2}
train['Embarked'] = train['Embarked'].map(embarked_mapping)
test['Embarked'] = test['Embarked'].map(embarked_mapping)

# %%
build_bar_chart('Title')

# %%
build_bar_chart('Sex')

# %% [markdown]
# this shows that **males are the most who died** in the accident

# %% [markdown]
# ## Model Building: Logistic Regression

# %%
# Separate target variable from features
from sklearn.model_selection import train_test_split
X = train.drop('Survived', axis=1)
y = train['Survived']

# Split the data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# %%
from sklearn.preprocessing import StandardScaler

# Initialize StandardScaler
scaler = StandardScaler()

# Identify numerical features to scale
numerical_cols = ['Age', 'Fare', 'FamilySize']

# Apply scaling to training and testing data
X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

print("Scaled training data head:")
display(X_train.head())
print("\nScaled testing data head:")
display(X_test.head())

# %%
from sklearn.linear_model import LogisticRegression

# Initialize and train the Logistic Regression model
logreg = LogisticRegression(
    solver='liblinear',
    random_state=42,
    max_iter=200
)
logreg.fit(X_train, y_train)

print("Logistic Regression model trained successfully.")

# %%
# Make predictions on the test set
y_pred = logreg.predict(X_test)

print("Predictions made on the test set.")

# %%
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def build_logistic_confusion_matrix(y_train, y_train_pred):

    cm = confusion_matrix(
        y_train,
        y_train_pred
    )

    fig, ax = plt.subplots(figsize=(5,5))

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm
    )

    disp.plot(ax=ax)

    ax.set_title("Logistic Regression Confusion Matrix")

    return fig

# %%
print(f"Test Accuracy: {test_acc_log*100:.2f}%")

# The confusion matrix provides a summary of prediction results on a classification problem.
# It shows the number of correct and incorrect predictions broken down by each class.
print("\nTest Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\n[[True Negatives (TN), False Positives (FP)]\n [False Negatives (FN), True Positives (TP)]])")

print("\nTest Classification Report:\n", classification_report(y_test, y_pred))

# %% [markdown]
# **Anlyzing to make sure from over fitting**

# %%
scores = [train_acc_log, test_acc_log]
labels = ['Train Accuracy', 'Test Accuracy']

plt.bar(labels, scores)
plt.ylim(0, 1)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()

# %%
import pandas as pd

def build_coefficient_matrix(model, X):

    feature_names = X.columns

    coefficients = model.coef_[0]

    coef_df = pd.DataFrame({

        "Feature": feature_names,

        "Coefficient": coefficients

    })

    return coef_df

coef_matrix = build_coefficient_matrix(
    logreg,
    X
)

print(coef_matrix)

# %% [markdown]
# Gender is the strongest predictor (**females more likely to survive**)
# 
# Higher class and higher fare
# **increase** survival chances
# 
# Larger families and being alone both **decrease** survival probability
# 
# Age slightly **decreases** survival

# %% [markdown]
# # Modeling using Decision Tree
# 

# %%
#To ensure from the pest Accuracy at Max_depth

# %%
from sklearn.tree  import DecisionTreeClassifier
depths= range(1,11)
accuracies =[]
for d in depths:
    dt_model = DecisionTreeClassifier(max_depth=d, random_state=42)
    dt_model.fit(X_train, y_train)

    pred = dt_model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    accuracies.append(acc)
    print(f"max_depth={d} -> accuracy={acc}")

# %%
plt.plot(depths, accuracies, marker='o')
plt.xlabel("max_depth")
plt.ylabel("Accuracy")
plt.title("Accuracy vs Tree Depth")
plt.show()

# %% [markdown]
# **the best Accuracy at Max_depth** =(4 ,5 , 6) we will **choose 4** to be more simple and avoid over fitting

# %%
model=DecisionTreeClassifier(max_depth=4,random_state=42)
model.fit(X_train,y_train)

# %%
predictions_test=model.predict(X_test)
predictions_train=model.predict(X_train)

# %%
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def build_dt_confusion_matrix(y_true, y_pred, model_name):

    cm = confusion_matrix(
        y_true,
        y_pred
    )

    fig, ax = plt.subplots(figsize=(5,5))

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm
    )

    disp.plot(ax=ax)

    ax.set_title(f"{model_name} Confusion Matrix")

    return fig

# %%
train_acc_dt = accuracy_score(y_train, predictions_train)
test_acc_dt = accuracy_score(y_test, predictions_test)
print (f" Test_acc = {test_acc_dt*100:.2f}%")
print (f"train_acc_dt = {train_acc_dt*100:.2f}%")

# %% [markdown]
# **Analyzing bar chart to make sure there is no over fitting**
# 

# %%
scores = [train_acc_dt, test_acc_dt]
labels = ['Train Accuracy', 'Test Accuracy']

plt.bar(labels, scores)
plt.ylim(0, 1)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()

# %%
import pandas as pd

def build_feature_importance_matrix(model, X):

    feature_names = X.columns

    importances = model.feature_importances_

    importance_df = pd.DataFrame({

        "Feature": feature_names,

        "Importance": importances

    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    return importance_df
importance_matrix = build_feature_importance_matrix(
    model,
    X
)

print(importance_matrix)

# %% [markdown]
# 
# 
# - **Title** is the strongest predictor of survival probability
# 
# - Higher passenger class (**Pclass**) and higher **Fare**
#   **increase** the chances of survival
# 
# - **Age** slightly affects survival probability
# 
# - **Sex** has an impact on survival prediction, although lower than Title
# 
# - **Embarked** has minimal influence on the model
# 
# - Features such as **SibSp**, **Parch**, **FamilySize**, and **Alone**
#   showed almost no impact on prediction results

# %%
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure( figsize=(10,6))
plot_tree(model,feature_names=X.columns,filled=True)
plt.title("Decision Tree")
plt.show()

# %% [markdown]
# ## Model Building: Support Vector Machine (SVM)

# %%
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# SVM is sensitive to feature scales, so we scale the data first
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svm_model = SVC(kernel='linear', C=1.0, gamma='scale', random_state=42)
svm_model.fit(X_train_scaled, y_train)
svm_pred = svm_model.predict(X_test_scaled)

# %%
svm_train_pred = svm_model.predict(X_train_scaled)
svm_train_accuracy=accuracy_score(y_train, svm_train_pred)
print(f"Training Accuracy: {svm_train_accuracy*100:.2f}%")

print("\nTraining Confusion Matrix:\n", confusion_matrix(y_train, svm_train_pred))
print("\n[[True Negatives (TN), False Positives (FP)]\n [False Negatives (FN), True Positives (TP)]])")

print("\nTraining Classification Report:\n", classification_report(y_train, svm_train_pred))

# %%
import pandas as pd

def build_svm_coefficients_matrix(model, X):

    feature_names = X.columns

    coefficients = model.coef_[0]

    coef_df = pd.DataFrame({

        "Feature": feature_names,

        "Coefficient": coefficients

    })

    coef_df = coef_df.sort_values(
        by="Coefficient",
        ascending=False
    )

    return coef_df

svm_coef_matrix = build_svm_coefficients_matrix(
    svm_model,
    X
)

print(svm_coef_matrix)

# %%
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def build_svm_confusion_matrix(y_train, svm_train_pred):

    cm = confusion_matrix(
        y_train,
        svm_train_pred
    )

    fig, ax = plt.subplots(figsize=(5,5))

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm
    )

    disp.plot(ax=ax)

    ax.set_title("SVM Confusion Matrix")

    return fig

# %%
test_acc_svm = accuracy_score(y_test, svm_pred)

print(f"Test Accuracy: {test_acc_svm*100:.2f}%")

print("\nTest Confusion Matrix:\n", confusion_matrix(y_test, svm_pred))
print("\n[[True Negatives (TN), False Positives (FP)]\n [False Negatives (FN), True Positives (TP)]])")

print("\nTest Classification Report:\n", classification_report(y_test, svm_pred))

# %% [markdown]
# **Analyzing to ensure no overfitting**

# %%
import matplotlib.pyplot as plt

train_acc = accuracy_score(y_train, svm_train_pred)
test_acc = accuracy_score(y_test, svm_pred)

plt.bar(['Train Accuracy', 'Test Accuracy'], [train_acc, test_acc])
plt.ylim(0, 1)
plt.title("SVM Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()

# %% [markdown]
# ## Model Building: Random Forest

# %%
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# %%
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)
rf_model.fit(X_train, y_train)
y_test_pred = rf_model.predict(X_test)
y_train_pred = rf_model.predict(X_train)
train_acc_rf=accuracy_score(y_train, y_train_pred)
test_acc_forest=accuracy_score(y_test, y_test_pred)
print(f"Training Accuracy:{train_acc_rf*100 :.2f}%")
print("\nTraining Confusion Matrix:\n", confusion_matrix(y_train, y_train_pred))
print("\n[[True Negatives (TN), False Positives (FP)]\n [False Negatives (FN), True Positives (TP)]])")
print("\nTraining Classification Report:\n", classification_report(y_train, y_train_pred))

# %%
#display confusion matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def build_rf_confusion_matrix(y_true, y_pred, model_name):

    cm = confusion_matrix(
        y_true,
        y_pred
    )

    fig, ax = plt.subplots()

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm
    )

    disp.plot(ax=ax)

    ax.set_title(f"{model_name} Confusion Matrix")

    return fig

# %%

print(f"Test Accuracy: {test_acc_forest*100:.2f}%")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, rf_pred))
print("\n[[True Negatives (TN), False Positives (FP)]\n [False Negatives (FN), True Positives (TP)]])")
print("\nClassification Report:\n", classification_report(y_test, rf_pred))

# %% [markdown]
# **Anlyzing to ensure from over fitting**

# %%
scores = [train_acc_rf, test_acc_forest]
labels = ['Train Accuracy', 'Test Accuracy']

plt.bar(labels, scores)
plt.ylim(0, 1)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()

# %%
import pandas as pd

def build_rf_feature_importance(rf_model, X):

    feature_names = X.columns

    importances = rf_model.feature_importances_

    importance_df = pd.DataFrame({

        "Feature": feature_names,

        "Importance": importances

    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    return importance_df

rf_importance_matrix = build_rf_feature_importance(
    rf_model,
    X
)

print(rf_importance_matrix)

# %% [markdown]
# 
# - **Title** is the strongest predictor of survival probability
# 
# - **Sex** also plays a major role in prediction
#   (**females were more likely to survive**)
# 
# - Higher **Fare** and better passenger class (**Pclass**)
#   **increase** the chances of survival
# 
# - **Age** has a moderate effect on survival prediction
# 
# - **FamilySize** and **SibSp** slightly influence survival outcomes
# 
# - **Embarked**, **Alone**, and **Parch**
#   have relatively small impact on the model predictions

# %%
import joblib
#joblib for the real models
joblib.dump(rf_model, "randomforest.pkl")

joblib.dump(logreg, "logistic.pkl")

joblib.dump(scaler, "scaler.pkl")
joblib.dump(svm_model, "svm.pkl")

joblib.dump(dt_model, "decision_tree.pkl")

#joblib for the accurcies
model_score={

"svm":test_acc_svm,
"dt":test_acc_dt,
"log":test_acc_log,
"Rf":test_acc_forest
}
joblib.dump(model_score,"acc.pkl")

#


# %%


