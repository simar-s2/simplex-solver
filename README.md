# Simplex Solver

A from-scratch implementation of the Simplex method for linear programming, with a
Streamlit front end for entering a problem and reading back the optimum.

> 🚧 **Work in progress.** Tableau construction and the optimality test are in
> place; the pivot step (`choose_pivot_row`, `perform_pivot`) and the Streamlit
> result wiring are still being built.

> 📸 **Screenshot needed**: the Streamlit page with the objective, constraint matrix, and RHS filled in, and a solved result below. Save to `docs/app.png` and replace this line with `![Simplex Solver UI](docs/app.png)`.

## Quickstart

```bash
git clone https://github.com/simar-s2/simplex-solver.git
cd simplex-solver

python -m venv venv                # Python 3.10
source venv/bin/activate           # Windows: venv\Scripts\activate
pip install -r requirements.txt

streamlit run app.py
```

## How it works

The solver (`simplex_solver.py`) works on the standard Simplex tableau for a
maximisation problem in the form `max cᵀx` subject to `Ax ≤ b`, `x ≥ 0`:

1. **Build the tableau.** Add one slack variable per constraint, stack `A | I | b`,
   and put the negated objective (`-c`) in the bottom row.
2. **Optimality test.** If no entry in the objective row is positive, the current
   basic solution is optimal.
3. **Choose the pivot column.** The most positive entry in the objective row (the
   variable that improves the objective fastest).
4. **Choose the pivot row.** The minimum-ratio test over `b_i / a_ij` for positive
   `a_ij`.
5. **Pivot.** Normalise the pivot row and eliminate the pivot column from every
   other row.
6. Repeat from step 2, keeping a copy of each tableau so the iterations can be
   inspected.

`app.py` is the Streamlit interface: it parses the objective coefficients, the
constraint matrix (one row per line), and the RHS vector from text inputs, then
calls `simplex()` and displays the optimal value and variable assignment.

## Layout

| File | Purpose |
|---|---|
| `simplex_solver.py` | the tableau and pivot logic |
| `app.py` | Streamlit UI |
| `test_solver.py` | a quick script that solves a sample 2-variable problem |

## Built with

Python 3.10 · NumPy · SciPy · Streamlit

## License

Released under the [MIT License](LICENSE).
