# Physics & Math Formula Solver

A desktop GUI application built with Python and Tkinter that solves multi-step Physics and Math problems across four topic modules.

Video Demo: Available on my portfolio at ompatel4723.github.io/Portfolio (under the Formula Solver card)

---

## Why I Built This

Before moving from India to the U.S. in May 2026 to finish my senior year at J.P. Stevens High School, I studied in the CBSE STEM stream (Physics, Chemistry, Math, and Informatics Practices), where Python was part of our coursework. I wanted to build something practical using Object-Oriented Programming (OOP) and GUI design to automate the exact kinematics, electricity, energy, and algebra formulas I was using in class.

Because Tkinter is a desktop GUI library, this app runs locally on your computer rather than directly inside a browser on GitHub Pages.

---

## Calculation Modules

### 1. Kinematics
* **Velocity Solver (v = u + at):** Enter any 3 values, and it calculates the 4th missing variable while showing the step-by-step math.
* **Projectile Motion:** Calculates horizontal range (R), max height (H), and time of flight (T) using initial speed and launch angle.

### 2. Energy & Power
* **Kinetic Energy (KE = 1/2 mv²):** Solves for kinetic energy, mass, or velocity given any two inputs.
* **Power Output (P = W/t):** Calculates power in Watts from work done and time.

### 3. Electricity
* **Ohm's Law (V = IR):** Quickly solves for voltage, current, or resistance.
* **Equivalent Resistance:** Computes both series (Rs) and parallel (Rp) resistance for a two-resistor circuit.

### 4. Math & Geometry
* **Quadratic Roots (ax² + bx + c = 0):** Finds the discriminant and outputs either real or complex roots.
* **2D Distance Formula:** Calculates the Euclidean distance between two coordinate points.

---

## Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter (`tkinter`, `ttk`, `messagebox`)
* **Standard Libraries:** `math`

---

## Repository Structure

```text
├── solver.py    # Complete OOP Tkinter application and formula calculation logic

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ompatel4723/Python-Project.git
   cd Python-Project
2. Run the application: (Tkinter is included with standard Python 3 installations on Windows and macOS)
   python solver.py