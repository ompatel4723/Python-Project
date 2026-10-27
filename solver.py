import math
import tkinter as tk
from tkinter import messagebox, ttk


class STEMCalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Problem Solver")
        self.root.geometry("620x700")
        self.root.resizable(False, False)

        # Main Header Section (Cleaned)
        header = tk.Frame(self.root, bg="#1e3d59", pady=15)
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="Physics & Math Solver",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#1e3d59",
        )
        title.pack()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=10)

        # Kinematics
        self.tab1 = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab1, text="Kinematics")
        self.build_kinematics_tab()

        # Energy & Power
        self.tab2 = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab2, text="Energy & Power")
        self.build_energy_tab()

        # Electricity
        self.tab3 = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab3, text="Electricity")
        self.build_electricity_tab()

        # Math & Geo
        self.tab4 = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab4, text="Math & Geometry")
        self.build_math_tab()

        # Output
        output_frame = ttk.LabelFrame(
            self.root, text=" Working & Calculation Output ", padding=10
        )
        output_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.output_text = tk.Text(
            output_frame,
            height=6,
            font=("Courier", 10),
            bg="#f8f9fa",
            relief="solid",
            bd=1,
        )
        self.output_text.pack(fill="both", expand=True, padx=5, pady=5)

        export_btn = ttk.Button(
            output_frame, text="Export Calculation Log", command=self.export_log
        )
        export_btn.pack(anchor="e", padx=5)

    # Function
    def parse_val(self, entry):
        text = entry.get().strip()
        if text == "":
            return None
        try:
            return float(text)
        except ValueError:
            return "ERROR"

    def write_output(self, msg):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, msg)

    def export_log(self):
        data = self.output_text.get("1.0", tk.END).strip()
        if not data:
            messagebox.showwarning("Warning", "No results to export.")
            return

        try:
            with open("stem_results_log.txt", "a") as f:
                f.write(data + "\n" + "-" * 40 + "\n")
            messagebox.showinfo(
                "Success", "Saved output to 'stem_results_log.txt'"
            )
        except Exception as err:
            messagebox.showerror("Error", f"Could not save file: {err}")

    # KINEMATICS
    def build_kinematics_tab(self):
        f1 = ttk.LabelFrame(
            self.tab1, text=" Velocity Solver (v = u + a*t) ", padding=10
        )
        f1.pack(fill="x", pady=5)

        ttk.Label(f1, text="Final Vel (v m/s):").grid(
            row=0, column=0, sticky="w", pady=2
        )
        self.v_entry = ttk.Entry(f1, width=8)
        self.v_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(f1, text="Initial Vel (u m/s):").grid(
            row=0, column=2, sticky="w", padx=(10, 0), pady=2
        )
        self.u_entry = ttk.Entry(f1, width=8)
        self.u_entry.grid(row=0, column=3, padx=5, pady=2)

        ttk.Label(f1, text="Accel (a m/s²):").grid(
            row=1, column=0, sticky="w", pady=2
        )
        self.a_entry = ttk.Entry(f1, width=8)
        self.a_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(f1, text="Time (t sec):").grid(
            row=1, column=2, sticky="w", padx=(10, 0), pady=2
        )
        self.t_entry = ttk.Entry(f1, width=8)
        self.t_entry.grid(row=1, column=3, padx=5, pady=2)

        ttk.Button(
            f1, text="Calculate Kinematics", command=self.solve_kinematics
        ).grid(row=2, column=0, columnspan=4, pady=8)

        f2 = ttk.LabelFrame(
            self.tab1, text=" Projectile Motion Analysis ", padding=10
        )
        f2.pack(fill="x", pady=5)

        ttk.Label(f2, text="Initial Speed (u m/s):").grid(
            row=0, column=0, sticky="w", pady=2
        )
        self.p_u_entry = ttk.Entry(f2, width=8)
        self.p_u_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(f2, text="Launch Angle (deg):").grid(
            row=0, column=2, sticky="w", padx=(10, 0), pady=2
        )
        self.p_deg_entry = ttk.Entry(f2, width=8)
        self.p_deg_entry.grid(row=0, column=3, padx=5, pady=2)

        ttk.Button(
            f2, text="Calculate Trajectory", command=self.solve_projectile
        ).grid(row=1, column=0, columnspan=4, pady=8)

    def solve_kinematics(self):
        v = self.parse_val(self.v_entry)
        u = self.parse_val(self.u_entry)
        a = self.parse_val(self.a_entry)
        t = self.parse_val(self.t_entry)

        if "ERROR" in (v, u, a, t):
            messagebox.showerror(
                "Input Error", "Please enter valid numeric values."
            )
            return

        given = [x for x in (v, u, a, t) if x is not None]
        if len(given) < 3:
            self.write_output(
                "INSUFFICIENT DATA:\nPlease fill at least 3 values."
            )
            return

        if v is None:
            res = u + (a * t)
            self.v_entry.insert(0, f"{res:.2f}")
            out = f"Final Velocity (v) = {res:.2f} m/s\nWorking: {u} + ({a} * {t})"
        elif u is None:
            res = v - (a * t)
            self.u_entry.insert(0, f"{res:.2f}")
            out = f"Initial Velocity (u) = {res:.2f} m/s\nWorking: {v} - ({a} * {t})"
        elif a is None:
            if t == 0:
                messagebox.showerror("Math Error", "Time cannot be 0.")
                return
            res = (v - u) / t
            self.a_entry.insert(0, f"{res:.2f}")
            out = f"Acceleration (a) = {res:.2f} m/s²\nWorking: ({v} - {u}) / {t}"
        elif t is None:
            if a == 0:
                messagebox.showerror("Math Error", "Acceleration cannot be 0.")
                return
            res = (v - u) / a
            self.t_entry.insert(0, f"{res:.2f}")
            out = f"Time (t) = {res:.2f} s\nWorking: ({v} - {u}) / {a}"
        else:
            out = (
                f"All values provided.\nFormula Check: {v} = {u} + ({a} * {t})"
            )

        self.write_output(f"=== KINEMATICS RESULT ===\n{out}")

    def solve_projectile(self):
        u = self.parse_val(self.p_u_entry)
        deg = self.parse_val(self.p_deg_entry)

        if u is None or deg is None or "ERROR" in (u, deg):
            self.write_output("ERROR: Speed and angle are required.")
            return

        g = 9.81
        rad = math.radians(deg)
        range_m = (u**2) * math.sin(2 * rad) / g
        height_m = ((u * math.sin(rad)) ** 2) / (2 * g)
        time_s = (2 * u * math.sin(rad)) / g

        out = (
            f"=== PROJECTILE MOTION ===\n"
            f"Speed: {u} m/s | Angle: {deg}° | Gravity: 9.81 m/s²\n"
            f"-----------------------------------------\n"
            f"Horizontal Range (R)  : {range_m:.2f} m\n"
            f"Max Height (H)        : {height_m:.2f} m\n"
            f"Time of Flight (T)    : {time_s:.2f} s"
        )
        self.write_output(out)

    # ENERGY & POWER
    def build_energy_tab(self):
        f1 = ttk.LabelFrame(
            self.tab2, text=" Kinetic Energy (KE = ½ * m * v²) ", padding=10
        )
        f1.pack(fill="x", pady=5)

        ttk.Label(f1, text="Kinetic Energy (J):").grid(
            row=0, column=0, sticky="w", pady=2
        )
        self.ke_entry = ttk.Entry(f1, width=8)
        self.ke_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(f1, text="Mass (kg):").grid(
            row=0, column=2, sticky="w", padx=(10, 0), pady=2
        )
        self.m_entry = ttk.Entry(f1, width=8)
        self.m_entry.grid(row=0, column=3, padx=5, pady=2)

        ttk.Label(f1, text="Velocity (m/s):").grid(
            row=1, column=0, sticky="w", pady=2
        )
        self.ke_v_entry = ttk.Entry(f1, width=8)
        self.ke_v_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Button(f1, text="Calculate KE", command=self.solve_ke).grid(
            row=2, column=0, columnspan=4, pady=8
        )

        f2 = ttk.LabelFrame(
            self.tab2, text=" Power (P = Work / Time) ", padding=10
        )
        f2.pack(fill="x", pady=5)

        ttk.Label(f2, text="Work Done (J):").grid(
            row=0, column=0, sticky="w", pady=2
        )
        self.w_entry = ttk.Entry(f2, width=8)
        self.w_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(f2, text="Time (sec):").grid(
            row=0, column=2, sticky="w", padx=(10, 0), pady=2
        )
        self.pw_t_entry = ttk.Entry(f2, width=8)
        self.pw_t_entry.grid(row=0, column=3, padx=5, pady=2)

        ttk.Button(f2, text="Calculate Power", command=self.solve_power).grid(
            row=1, column=0, columnspan=4, pady=8
        )

    def solve_ke(self):
        ke = self.parse_val(self.ke_entry)
        m = self.parse_val(self.m_entry)
        v = self.parse_val(self.ke_v_entry)

        if "ERROR" in (ke, m, v):
            messagebox.showerror("Error", "Please enter numbers only.")
            return

        given = [x for x in (ke, m, v) if x is not None]
        if len(given) < 2:
            self.write_output(
                "INSUFFICIENT DATA:\nPlease fill at least 2 fields."
            )
            return

        if ke is None:
            res = 0.5 * m * (v**2)
            self.ke_entry.insert(0, f"{res:.2f}")
            out = f"Kinetic Energy = {res:.2f} J"
        elif m is None:
            if v == 0:
                messagebox.showerror("Error", "Velocity cannot be 0.")
                return
            res = (2 * ke) / (v**2)
            self.m_entry.insert(0, f"{res:.2f}")
            out = f"Mass = {res:.2f} kg"
        elif v is None:
            if m == 0:
                messagebox.showerror("Error", "Mass cannot be 0.")
                return
            res = math.sqrt((2 * ke) / m)
            self.ke_v_entry.insert(0, f"{res:.2f}")
            out = f"Velocity = {res:.2f} m/s"
        else:
            out = f"All fields filled. KE = {0.5 * m * (v**2):.2f} J"

        self.write_output(f"=== KINETIC ENERGY ===\n{out}")

    def solve_power(self):
        w = self.parse_val(self.w_entry)
        t = self.parse_val(self.pw_t_entry)

        if w is None or t is None or "ERROR" in (w, t):
            self.write_output("ERROR: Both Work and Time are required.")
            return

        if t <= 0:
            messagebox.showerror("Error", "Time must be greater than 0.")
            return

        p = w / t
        self.write_output(
            f"=== POWER OUTPUT ===\nPower = {p:.2f} Watts (W)\nWorking: {w} J / {t} s"
        )

    # ELECTRICITY
    def build_electricity_tab(self):
        f1 = ttk.LabelFrame(
            self.tab3, text=" Ohm's Law Solver (V = I * R) ", padding=10
        )
        f1.pack(fill="x", pady=5)

        ttk.Label(f1, text="Voltage (V):").grid(
            row=0, column=0, sticky="w", pady=2
        )
        self.v_ohm = ttk.Entry(f1, width=8)
        self.v_ohm.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(f1, text="Current (I Amps):").grid(
            row=0, column=2, sticky="w", padx=(10, 0), pady=2
        )
        self.i_ohm = ttk.Entry(f1, width=8)
        self.i_ohm.grid(row=0, column=3, padx=5, pady=2)

        ttk.Label(f1, text="Resistance (R Ω):").grid(
            row=1, column=0, sticky="w", pady=2
        )
        self.r_ohm = ttk.Entry(f1, width=8)
        self.r_ohm.grid(row=1, column=1, padx=5, pady=2)

        ttk.Button(f1, text="Solve Ohm's Law", command=self.solve_ohm).grid(
            row=2, column=0, columnspan=4, pady=8
        )

        f2 = ttk.LabelFrame(
            self.tab3, text=" Equivalent Resistance (R1 & R2) ", padding=10
        )
        f2.pack(fill="x", pady=5)

        ttk.Label(f2, text="Resistor 1 (R1 Ω):").grid(
            row=0, column=0, sticky="w", pady=2
        )
        self.r1_entry = ttk.Entry(f2, width=8)
        self.r1_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(f2, text="Resistor 2 (R2 Ω):").grid(
            row=0, column=2, sticky="w", padx=(10, 0), pady=2
        )
        self.r2_entry = ttk.Entry(f2, width=8)
        self.r2_entry.grid(row=0, column=3, padx=5, pady=2)

        ttk.Button(
            f2, text="Calculate Circuits", command=self.solve_resistors
        ).grid(row=1, column=0, columnspan=4, pady=8)

    def solve_ohm(self):
        v = self.parse_val(self.v_ohm)
        i = self.parse_val(self.i_ohm)
        r = self.parse_val(self.r_ohm)

        if "ERROR" in (v, i, r):
            messagebox.showerror("Error", "Invalid numeric input.")
            return

        given = [x for x in (v, i, r) if x is not None]
        if len(given) < 2:
            self.write_output(
                "INSUFFICIENT DATA:\nPlease fill at least 2 fields."
            )
            return

        if v is None:
            res = i * r
            self.v_ohm.insert(0, f"{res:.2f}")
            out = f"Voltage (V) = {res:.2f} Volts"
        elif i is None:
            if r == 0:
                messagebox.showerror("Error", "Resistance cannot be 0.")
                return
            res = v / r
            self.i_ohm.insert(0, f"{res:.2f}")
            out = f"Current (I) = {res:.2f} Amps"
        elif r is None:
            if i == 0:
                messagebox.showerror("Error", "Current cannot be 0.")
                return
            res = v / i
            self.r_ohm.insert(0, f"{res:.2f}")
            out = f"Resistance (R) = {res:.2f} Ω"
        else:
            out = f"All fields filled. V = {i * r:.2f} Volts"

        self.write_output(f"=== OHM'S LAW ===\n{out}")

    def solve_resistors(self):
        r1 = self.parse_val(self.r1_entry)
        r2 = self.parse_val(self.r2_entry)

        if r1 is None or r2 is None or "ERROR" in (r1, r2):
            self.write_output("ERROR: Both R1 and R2 values are required.")
            return

        if r1 <= 0 or r2 <= 0:
            messagebox.showerror("Error", "Resistor values must be > 0.")
            return

        r_seq = r1 + r2
        r_par = (r1 * r2) / (r1 + r2)

        out = (
            f"=== EQUIVALENT RESISTANCE ===\nR1: {r1} Ω | R2: {r2} Ω\n"
            f"Series  (Rs) = {r_seq:.2f} Ω\nParallel (Rp) = {r_par:.2f} Ω"
        )
        self.write_output(out)

    # MATH & GEO
    def build_math_tab(self):
        f1 = ttk.LabelFrame(
            self.tab4, text=" Quadratic Roots (ax² + bx + c = 0) ", padding=10
        )
        f1.pack(fill="x", pady=5)

        ttk.Label(f1, text="a:").grid(row=0, column=0, sticky="w", pady=2)
        self.a_quad = ttk.Entry(f1, width=6)
        self.a_quad.grid(row=0, column=1, padx=4, pady=2)

        ttk.Label(f1, text="b:").grid(
            row=0, column=2, sticky="w", padx=(10, 0), pady=2
        )
        self.b_quad = ttk.Entry(f1, width=6)
        self.b_quad.grid(row=0, column=3, padx=4, pady=2)

        ttk.Label(f1, text="c:").grid(
            row=0, column=4, sticky="w", padx=(10, 0), pady=2
        )
        self.c_quad = ttk.Entry(f1, width=6)
        self.c_quad.grid(row=0, column=5, padx=4, pady=2)

        ttk.Button(f1, text="Solve Quadratic", command=self.solve_quadratic).grid(
            row=1, column=0, columnspan=6, pady=8
        )

        f2 = ttk.LabelFrame(
            self.tab4, text=" 2D Distance Formula ", padding=10
        )
        f2.pack(fill="x", pady=5)

        ttk.Label(f2, text="P1 (x1, y1):").grid(
            row=0, column=0, sticky="w", pady=2
        )
        self.x1_e = ttk.Entry(f2, width=5)
        self.x1_e.grid(row=0, column=1, padx=2, pady=2)
        self.y1_e = ttk.Entry(f2, width=5)
        self.y1_e.grid(row=0, column=2, padx=2, pady=2)

        ttk.Label(f2, text="P2 (x2, y2):").grid(
            row=0, column=3, sticky="w", padx=(10, 0), pady=2
        )
        self.x2_e = ttk.Entry(f2, width=5)
        self.x2_e.grid(row=0, column=4, padx=2, pady=2)
        self.y2_e = ttk.Entry(f2, width=5)
        self.y2_e.grid(row=0, column=5, padx=2, pady=2)

        ttk.Button(
            f2, text="Calculate Distance", command=self.solve_distance
        ).grid(row=1, column=0, columnspan=6, pady=8)

    def solve_quadratic(self):
        a = self.parse_val(self.a_quad)
        b = self.parse_val(self.b_quad)
        c = self.parse_val(self.c_quad)

        if a is None or b is None or c is None or "ERROR" in (a, b, c):
            self.write_output("ERROR: All coefficients (a, b, c) required.")
            return

        if a == 0:
            messagebox.showerror(
                "Error", "Coefficient 'a' cannot be 0 for quadratic."
            )
            return

        disc = (b**2) - (4 * a * c)

        if disc < 0:
            real = -b / (2 * a)
            imag = math.sqrt(-disc) / (2 * a)
            roots = f"Complex Roots:\nx1 = {real:.2f} + {imag:.2f}i\nx2 = {real:.2f} - {imag:.2f}i"
        else:
            x1 = (-b + math.sqrt(disc)) / (2 * a)
            x2 = (-b - math.sqrt(disc)) / (2 * a)
            roots = f"Real Roots:\nx1 = {x1:.2f}\nx2 = {x2:.2f}"

        self.write_output(
            f"=== QUADRATIC SOLVER ===\nDiscriminant (D) = {disc:.2f}\n{roots}"
        )

    def solve_distance(self):
        x1 = self.parse_val(self.x1_e)
        y1 = self.parse_val(self.y1_e)
        x2 = self.parse_val(self.x2_e)
        y2 = self.parse_val(self.y2_e)

        if (
            x1 is None
            or y1 is None
            or x2 is None
            or y2 is None
            or "ERROR" in (x1, y1, x2, y2)
        ):
            self.write_output("ERROR: All 4 coordinates required.")
            return

        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.write_output(
            f"=== 2D DISTANCE ===\nP1({x1}, {y1}) to P2({x2}, {y2})\nDistance = {dist:.2f} units"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = STEMCalculatorApp(root)
    root.mainloop()