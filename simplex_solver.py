# simplex_solver.py
import numpy as np

def create_simplex_tableau(c, A, b):
    # Step 2: Set up the initial tableau here
    def create_simplex_tableau(c, A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    num_constraints, num_variables = A.shape

    # Add slack variables
    A_slack = np.hstack([A, np.eye(num_constraints)])

    # Append b (RHS)
    tableau_upper = np.hstack([A_slack, b.reshape(-1, 1)])

    # Objective row (note: -c for maximization)
    c_row = np.hstack([-c, np.zeros(num_constraints + 1)])

    # Combine into full tableau
    tableau = np.vstack([tableau_upper, c_row])

    return tableau

def optimal(tableau):
    # Step 3.1: check if optimal solution is reached
    objective_row = tableau[-1, :-1]  # Exclude the RHS
    return np.all(objective_row <= 0)

def choose_pivot_column(tableau):
    # Step 3.2: pick most negative value in last row
    pivot_col = np.argmax(tableau[-1, :-1])
    if tableau[-1, pivot_col] <= 0:
    # Already optimal
        return None

def choose_pivot_row(tableau, pivot_col):
    # Step 3.3: ratio test
    pass

def perform_pivot(tableau, pivot_row, pivot_col):
    # Step 3.4: update tableau
    pass

def simplex(c, A, b):
    # The main function that calls all the above
    steps = []
    tableau = create_simplex_tableau(c, A, b)
    steps.append(tableau.copy())

    while not optimal(tableau):
        pivot_col = choose_pivot_column(tableau)
        pivot_row = choose_pivot_row(tableau, pivot_col)
        tableau = perform_pivot(tableau, pivot_row, pivot_col)
        steps.append(tableau.copy())

    return steps, tableau