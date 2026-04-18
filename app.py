import streamlit as st

st.set_page_config(page_title="Stoping Method Selector", layout="centered")

st.title("Sequential Stoping Method Selection Tool")

# -----------------------------
# METHOD DATABASE (LOGIC BASE)
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

# -----------------------------
# PARAMETER ORDER
# -----------------------------
parameters = [
    "Ore Strength",
    "Rock Strength",
    "Shape",
    "Dip",
    "Size",
    "Grade",
    "Uniformity",
    "Depth"
]

# -----------------------------
# SESSION STATE
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.selections = {}
    st.session_state.valid_methods = list(methods_db.keys())

# -----------------------------
# FUNCTION: FILTER METHODS
# -----------------------------
def filter_methods(param, value):
    valid = []
    for method, conditions in methods_db.items():
        if method in st.session_state.valid_methods:
            if value in conditions[param]:
                valid.append(method)
    return valid

# -----------------------------
# FUNCTION: GET NEXT OPTIONS
# -----------------------------
def get_possible_values(param):
    values = set()
    for method in st.session_state.valid_methods:
        values.update(methods_db[method][param])
    return list(values)

# -----------------------------
# MAIN FLOW
# -----------------------------
if st.session_state.step < len(parameters):

    current_param = parameters[st.session_state.step]

    st.subheader(f"Select {current_param}")

    options = get_possible_values(current_param)

    if not options:
        st.error("Not economical to mine (No valid method for this combination)")
        st.stop()

    choice = st.selectbox("Choose value", options)

    if st.button("Next"):
        st.session_state.selections[current_param] = choice

        # Filter methods
        st.session_state.valid_methods = filter_methods(current_param, choice)

        if not st.session_state.valid_methods:
            st.error("Not economical to mine (No matching method)")
            st.stop()

        st.session_state.step += 1
        st.rerun()

# -----------------------------
# FINAL RESULT
# -----------------------------
else:
    st.success("Possible Stoping Methods:")

    for method in st.session_state.valid_methods:
        st.write(f"- {method}")

    if len(st.session_state.valid_methods) == 1:
        st.success(f"Recommended Method: {st.session_state.valid_methods[0]}")

    st.write("### Selected Conditions:")
    st.write(st.session_state.selections)

    if st.button("Restart"):
        st.session_state.step = 0
        st.session_state.selections = {}
        st.session_state.valid_methods = list(methods_db.keys())
        st.rerun()