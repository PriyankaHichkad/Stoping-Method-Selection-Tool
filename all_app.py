import streamlit as st
import pandas as pd

st.set_page_config(page_title="Stoping Method Selector", layout="wide")

st.title("Stoping Method Selection Tool")

# -----------------------------
# METHOD DATABASE (YOUR UPDATED)
# -----------------------------
methods_db = {
    "Shrinkage Stoping": {
        "Ore Strength": ["Strong"],
        "Rock Strength": ["Strong"],
        "Shape": ["Tabular", "Lenticular"],
        "Dip": ["Steep"],
        "Size": ["Thin", "Moderate"],
        "Grade": ["High"],
        "Uniformity": ["Uniform"],
        "Depth": ["Shallow", "Moderate"]
    },
    "Cut & Fill": {
        "Ore Strength": ["Moderate", "Strong"],
        "Rock Strength": ["Weak"],
        "Shape": ["Tabular", "Irregular"],
        "Dip": ["Moderate", "Steep"],
        "Size": ["Thin", "Moderate"],
        "Grade": ["High"],
        "Uniformity": ["Variable", "Moderate"],
        "Depth": ["Moderate", "Deep"]
    },
    "Stull": {
        "Ore Strength": ["Strong"],
        "Rock Strength": ["Moderate"],
        "Shape": ["Tabular", "Irregular"],
        "Dip": ["Moderate", "Steep"],
        "Size": ["Thin"],
        "Grade": ["High"],
        "Uniformity": ["Variable", "Moderate"],
        "Depth": ["Moderate"]
    },
    "Sublevel Stoping": {
        "Ore Strength": ["Moderate", "Strong"],
        "Rock Strength": ["Strong"],
        "Shape": ["Tabular", "Lenticular"],
        "Dip": ["Steep"],
        "Size": ["Moderate", "Thick"],
        "Grade": ["Moderate", "High"],
        "Uniformity": ["Uniform"],
        "Depth": ["Moderate"]
    },
    "Block Caving": {
        "Ore Strength": ["Weak", "Moderate"],
        "Rock Strength": ["Weak", "Moderate"],
        "Shape": ["Tabular"],
        "Dip": ["Steep"],
        "Size": ["Thick"],
        "Grade": ["Low", "Moderate", "High"],
        "Uniformity": ["Uniform"],
        "Depth": ["Moderate"]
    },
    "Longwall": {
        "Ore Strength": ["Weak", "Moderate", "Strong"],
        "Rock Strength": ["Weak", "Moderate"],
        "Shape": ["Tabular"],
        "Dip": ["Flat"],
        "Size": ["Thin"],
        "Grade": ["Moderate", "High"],
        "Uniformity": ["Uniform"],
        "Depth": ["Moderate", "Deep"]
    },
    "Sublevel Caving": {
        "Ore Strength": ["Moderate", "Strong"],
        "Rock Strength": ["Weak", "Moderate", "Strong"],
        "Shape": ["Tabular"],
        "Dip": ["Steep"],
        "Size": ["Thick"],
        "Grade": ["Moderate", "High"],
        "Uniformity": ["Moderate"],
        "Depth": ["Moderate"]
    },
    "Square Set": {
        "Ore Strength": ["Weak"],
        "Rock Strength": ["Weak"],
        "Shape": ["Tabular", "Lenticular", "Irregular"],
        "Dip": ["Steep", "Moderate", "Flat"],
        "Size": ["Thick", "Thin", "Moderate"],
        "Grade": ["High"],
        "Uniformity": ["Variable"],
        "Depth": ["Deep"]
    },
    "Room & Pillar": {
        "Ore Strength": ["Moderate", "Weak"],
        "Rock Strength": ["Moderate", "Strong"],
        "Shape": ["Tabular"],
        "Dip": ["Flat"],
        "Size": ["Thin"],
        "Grade": ["High", "Moderate"],
        "Uniformity": ["Uniform"],
        "Depth": ["Shallow", "Moderate"]
    },
    "Stope & Pillar": {
        "Ore Strength": ["Moderate", "Strong"],
        "Rock Strength": ["Moderate", "Strong"],
        "Shape": ["Tabular", "Lenticular"],
        "Dip": ["Flat", "Moderate"],
        "Size": ["Thin", "Thick", "Moderate"],
        "Grade": ["High", "Moderate", "Low"],
        "Uniformity": ["Variable"],
        "Depth": ["Shallow", "Moderate"]
    }
}

parameters = list(next(iter(methods_db.values())).keys())

# -----------------------------
# USER INPUT (ALL AT ONCE)
# -----------------------------
inputs = {}

st.sidebar.header("Input Parameters")

for param in parameters:
    options = set()
    for m in methods_db.values():
        options.update(m[param])
    inputs[param] = st.sidebar.selectbox(param, sorted(list(options)))

# -----------------------------
# STRICT MATCH
# -----------------------------
valid_methods = []

for method, conditions in methods_db.items():
    match = True
    for param in parameters:
        if inputs[param] not in conditions[param]:
            match = False
            break
    if match:
        valid_methods.append(method)

# -----------------------------
# FALLBACK SCORING
# -----------------------------
scores = {}

for method, conditions in methods_db.items():
    score = 0
    for param in parameters:
        if inputs[param] in conditions[param]:
            score += 1
    scores[method] = score

df = pd.DataFrame(scores.items(), columns=["Method", "Score"])
df = df.sort_values(by="Score", ascending=False)

# -----------------------------
# OUTPUT
# -----------------------------
st.subheader("Results")

if valid_methods:
    st.success("Exact Match Found!")
    for m in valid_methods:
        st.write(f"- {m}")
    st.success(f"Recommended Method: {valid_methods[0]}")
else:
    st.warning("No exact match found → Showing closest possible method")

    best_method = df.iloc[0]["Method"]

    st.success(f"Recommended Method (Best Fit): {best_method}")

st.bar_chart(df.set_index("Method"))

st.write("### Input Conditions")
st.write(inputs)