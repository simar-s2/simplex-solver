# app.py
import streamlit as st
from simplex_solver import simplex
import numpy as np

st.title("📈 Simplex Solver")

st.markdown("Enter your linear programming problem below:")

c_input = st.text_input("Objective Function Coefficients (e.g., 3,2)")
A_input = st.text_area("Constraint Matrix A (rows comma-separated)", height=100)
b_input = st.text_input("Right-hand side b (e.g., 8,16)")

if st.button("Solve"):
    try:
        c = [float(x) for x in c_input.split(",")]
        A = [[float(num) for num in row.split(",")] for row in A_input.strip().split("\n")]
        b = [float(x) for x in b_input.split(",")]

        result = simplex(c, A, b)
        if result.success:
            st.success("Optimal Solution Found")
            st.write("Optimal value:", -result.fun)
            st.write("x =", result.x)
        else:
            st.error("No solution found.")
    except Exception as e:
        st.error(f"Error: {e}")