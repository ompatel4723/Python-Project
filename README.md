# Physics & Math Formula Solver

A desktop GUI application built with Python and Tkinter that automates multi-step Physics and Mathematics problems across four topic modules.

**Video Demo:** Available on my main portfolio at [ompatel4723.github.io/Portfolio](https://ompatel4723.github.io/Portfolio/) *(under the Formula Solver project card)*

---

## Why I Built This

Before relocating from India to the U.S. in May 2026, I studied in the CBSE STEM stream (Physics, Chemistry, Mathematics, and Informatics Practices), where Python was part of my coursework. I built this project to apply Object-Oriented Programming (OOP) and GUI design to the exact kinematics, electricity, energy, and algebra formulas I used in class.

*(Note: Because Tkinter is a native desktop GUI library, this application cannot run directly inside a web browser on GitHub Pages. You can watch a full screen recording of the app running via the **Watch Demo** button on my portfolio site, or run `solver.py` locally using the steps below.)*

---

## Calculation Modules

### 1. Kinematics
- **Velocity Solver (v=u+at):** Solves for any single missing variable (final velocity, initial velocity, acceleration, or time) when the other three are entered, automatically filling the empty input field and displaying the step-by-step substitution.
- **Projectile Motion Analysis:** Computes horizontal range (R), maximum height (H), and total time of flight (T) from initial speed and launch angle using standard gravity (g=9.81m/s2).

### 2. Energy & Power
- **Kinetic Energy (KE=12mv2):** Dynamically solves for kinetic energy, mass, or velocity when any two values are provided.
- **Power Output (P=Wt):** Calculates power in Watts (W) from work done (J) and elapsed time (s).

### 3. Electricity
- **Ohm's Law Solver (V=IR):** Solves for voltage, current, or resistance given the remaining two values.
- **Equivalent Resistance (R1 & R2):** Calculates both series (Rs=R1+R2) and parallel (Rp=R1R2R1+R2) resistance for two-resistor circuits.

### 4. Math & Geometry
- **Quadratic Roots (ax2+bx+c=0):** Evaluates the discriminant (D=b2-4ac) to output either real roots or complex conjugate roots (x=realimagi).
- **2D Distance Formula:** Calculates Euclidean distance between two coordinate points P1(x1,y1) and P2(x2,y2).

---

## Key Features

- **Tabbed Interface:** Uses `ttk.Notebook` and `LabelFrame` containers to organize 8 formula solvers cleanly across 4 category tabs.
- **Step-by-Step Output Console:** Displays formatted equations, intermediate working, and final units inside a monospace `Courier` output box.
- **Calculation Log Export:** Clicking **Export Calculation Log** appends the current output to a local `stem_results_log.txt` file with section dividers for later review.
- **Input Validation & Error Handling:** Catches non-numeric entries, missing fields, and division-by-zero edge cases (such as t=0, a=0, or zero resistance) using `tkinter.messagebox` alerts.

---

## Tech Stack

- **Language:** Python 3
- **GUI Framework:** Tkinter (`tkinter`, `ttk`, `messagebox`)
- **Standard Libraries:** `math`

---

## Repository Structure

```text
└── solver.py           # Complete OOP Tkinter application and formula solvers
```

---

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone (https://github.com/ompatel4723/Python-Project.git)
   cd Python-Project
   ```

2. **Run the application:**
   *(Tkinter is included with standard Python 3 installations on Windows and macOS)*
   ```bash
   python solver.py
   ```

