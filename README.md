# Physics & Math Formula Solver

A desktop GUI app built with Python and Tkinter that solves multi-step Physics and Math problems across four topic modules. 

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)](https://docs.python.org/3/library/tkinter.html)

---

## Why I Built This

Before moving from India to the U.S., I studied in the CBSE STEM stream (Physics, Chemistry, Math, and Informatics Practices), where Python was part of our coursework. I wanted to build something practical using Object-Oriented Programming (OOP) and GUI design to automate the exact kinematics, electricity, energy, and algebra formulas I was using in class.

> **Note:** Because Tkinter is a desktop GUI library, this app runs locally on your machine rather than directly inside a browser on GitHub Pages. You can watch a full video demo of it running on my [portfolio site](https://ompatel4723.github.io/Portfolio/) (under the Formula Solver card), or just clone the repo and run it yourself!

---

## What's Inside (Calculation Modules)

### 1. Kinematics
* **Velocity Solver ($v = u + at$):** Enter any 3 values, and it calculates the 4th missing variable while showing the step-by-step math.
* **Projectile Motion:** Calculates horizontal range ($R$), max height ($H$), and time of flight ($T$) using your initial speed and launch angle.

### 2. Energy & Power
* **Kinetic Energy ($KE = \frac{1}{2}mv^2$):** Solves for kinetic energy, mass, or velocity given any two inputs.
* **Power Output ($P = W/t$):** Calculates power in Watts from work done and time.

### 3. Electricity
* **Ohm's Law ($V = IR$):** Quickly solves for voltage, current, or resistance.
* **Equivalent Resistance:** Computes both series ($R_s$) and parallel ($R_p$) resistance for a two-resistor circuit.

### 4. Math & Geometry
* **Quadratic Roots ($ax^2 + bx + c = 0$):** Finds the discriminant and outputs either real or complex roots.
* **2D Distance Formula:** Calculates the Euclidean distance between two coordinate points.

---

## Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter (`tkinter`, `ttk`, `messagebox`)
* **Libraries:** `math`

---

## How to Run It Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/ompatel4723/Python-Project.git
   cd Python-Project

2. Run the script:
(Tkinter comes built-in with standard Python installations)
   python solver.py
