---
TITLE: Stoping-Method-Selection-Tool
AUTHOR: Priyanka Rajeev Hichkad
---

## Overview

This project presents an advanced decision-support system for selecting the most suitable underground stoping method. 

It integrates:
- A constraint-based filtering model
- A fallback scoring mechanism (best-fit selection)
- An interactive Streamlit web application
- A physical model representation of parameters

Unlike traditional systems, this tool ensures that a method is always recommended, even for non-ideal conditions.

---

## Objective
- Develop a structured and logical approach to stoping method selection
- Convert geological parameters into decision rules
- Avoid system failure by implementing a best-fit fallback mechanism
- Provide both digital and physical visualization of decision-making

---

## Methodology

1. Constraint-Based Filtering
- User inputs mining parameters
- Methods are filtered based on strict feasibility conditions
- Only methods satisfying all conditions are considered valid

2. Fallback Scoring System (Key Innovation)

If no exact match exists:
- Each method is evaluated based on partial matches
- Score is calculated as: Number of matching parameters
- The method with the highest score is selected

3. Final Decision Logic
- Condition	Output
- Exact match exists	Show valid method(s)
- No match exists	Show best-fit method
- All cases	Always return a result

---

## Parameters Considered
- Ore Strength
- Rock Strength
- Deposit Shape
- Deposit Dip
- Deposit Size
- Ore Grade
- Ore Uniformity
- Depth

---

## Stoping Methods Included
- Shrinkage Stoping
- Cut & Fill
- Stull Stoping
- Sublevel Stoping
- Block Caving
- Longwall
- Sublevel Caving
- Square Set
- Room & Pillar
- Stope & Pillar

---

## Streamlit Application

### Features
- User-friendly sidebar input system
- Exact match detection
- Intelligent fallback recommendation

### Visual comparison using bar charts
- Always produces a valid output

### Run Locally
```bash
pip install streamlit pandas
streamlit run app.py
```

### Decision Logic Explained
- Collect user inputs
- Check for exact match with method database
- If match exists → return method
- Else: Compute similarity score & Select closest matching method

### Integration with Physical Model
- Digital System:	Physical Model
- Input parameters:	Rotating blocks
- Filtering logic:	Path restriction
- Final method:	Highlighted column

---

## Key Insight

This project demonstrates how a strict engineering decision system can be enhanced with:

- Flexibility (fallback logic)
- Robustness (no failure cases)
- Practical usability (real-world applicability)

---

## Future Improvements
- Introduce weighted scoring instead of equal scoring
- Add economic cost analysis module
- Integrate real mining datasets
- Deploy as a web-based decision support system

Developed as part of a Underground Metal Mining Project

---

## Contribution

Contributions are welcome!

Steps to contribute:

- Fork the repository
- Create a new branch
- Make your changes
- Submit a Pull Request
