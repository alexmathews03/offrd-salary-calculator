# Salary Breakdown Calculator

**Evaluation Exercise — Part C (Option 1) for Offrd Product Engineering Intern Assignment**

A robust Python module, CLI tool, and interactive web dashboard that takes an annual Cost-to-Company (CTC) in INR and computes a detailed monthly payroll breakdown compliant with Indian statutory regulations.

---

## Features

- **Monthly Breakdown Components:**
  - Basic Salary (50% of CTC)
  - House Rent Allowance (HRA, 50% of Basic)
  - Special Allowance (Balancing Component)
  - Gross Monthly Salary
  - Employer & Employee EPF (Provident Fund)
  - Employer & Employee ESI (State Insurance)
  - Professional Tax (PT)
  - Net Take-Home Pay
- **Statutory Edge-Case Handling:**
  - **ESI Threshold Detection:** Automatically triggers ESI contributions (0.75% employee, 3.25% employer) when Gross Monthly Salary $\le$ ₹21,000/month.
  - **EPF Statutory Ceiling:** Accurately caps EPF calculation at the statutory basic limit of ₹15,000/month (max ₹1,800/month contribution each for employer and employee).
  - **Low CTC Floor Guard:** Prevents negative Special Allowance on entry-level compensation packages.
- **Multiple Execution Interfaces:**
  - **Interactive Web App:** Real-time visual dashboard built with Flask.
  - **Command-Line Interface (CLI):** Instant terminal printout with formatted salary slip.
- **Unit Tested:** 100% test pass rate across 5 distinct test scenarios using `pytest`.

---

## Assumptions Made

1. **Basic Salary:** Set at **50% of monthly CTC**, conforming to modern Indian compensation restructuring norms.
2. **HRA (House Rent Allowance):** Set at **50% of Basic Salary** (standard for metro locations).
3. **EPF (Employee Provident Fund):**
   - Statutory wage ceiling is **₹15,000/month**.
   - Contribution is **12%** of the capped basic for both Employee and Employer (maximum contribution of ₹1,800/month each).
4. **ESI (Employee State Insurance):**
   - Applicable **only** when Gross Monthly Salary is **$\le$ ₹21,000/month**.
   - Employee Contribution: **0.75%** of Gross Salary.
   - Employer Contribution: **3.25%** of Gross Salary.
   - For employees earning over ₹21,000/month, ESI is ₹0.
5. **Special Allowance:** Acts as the balancing component ensuring Gross Salary equals Basic + HRA + Special Allowance.
6. **Professional Tax (PT):** Standard Indian state slab of **₹200/month** for gross monthly earnings exceeding ₹15,000.

---

## Edge Cases Handled

1. **The ESI Threshold (Gross $\le$ ₹21,000/mo):**
   - Handled dynamically: For lower CTCs (e.g., ₹1.8 LPA), ESI rates are automatically computed and deducted. For higher CTCs (e.g., ₹6 LPA), ESI automatically turns off.
2. **The EPF Statutory Ceiling Cap:**
   - For high salaries (e.g., ₹24 LPA), EPF does not escalate unchecked to 12% of ₹1,00,000 basic; it correctly caps at 12% of ₹15,000 (₹1,800/mo).
3. **Very Low CTC Floor:**
   - Prevents negative Special Allowance or negative Net Take-Home on entry-level compensation.
4. **Input Validation:**
   - Raises informative `ValueError` on zero or negative CTC inputs.

---

## How to Run

### 1. Prerequisites
- Python 3.8+ installed.

Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Option A: Run the Interactive Web App (Recommended)
Launch the Flask web server:
```bash
python app.py
```
Then open your browser and navigate to:
```
http://127.0.0.1:5000
```
You can type any annual CTC or use quick preset buttons (₹1.8 LPA ESI test, ₹6 LPA mid-level, ₹24 LPA executive) to see real-time recalculations and visual badges!

### 3. Option B: Run via Command Line (CLI)
Pass any annual CTC amount (in INR) as an argument:
```bash
python salary_calculator.py 600000
```
Or test low CTC with ESI:
```bash
python salary_calculator.py 180000
```

### 4. Option C: Run the Unit Tests
Execute the test suite with `pytest`:
```bash
pytest test_calculator.py -v
```

---

## Project Structure

```text
offrd-salary-calculator/
├── app.py                 # Flask web application server
├── templates/
│   └── index.html         # Modern responsive web UI
├── salary_calculator.py   # Core payroll calculation engine & CLI
├── test_calculator.py     # Unit test suite covering multiple CTC levels & edge cases
├── requirements.txt       # Project dependencies (Flask, pytest)
├── .gitignore             # Standard Python ignore rules
└── README.md              # Project documentation, assumptions, and edge cases
```

---

## What I Would Do With More Time

1. **Configurable Structure Profiles:** Allow custom configuration of Basic percentage (40% vs 50%) and HRA (Metro 50% vs Non-Metro 40%).
2. **State-Wise Professional Tax Tables:** Dynamically calculate PT based on state-specific tax slabs (e.g., Karnataka vs Maharashtra vs Delhi).
3. **Income Tax (TDS) Projections:** Add an estimated monthly TDS deduction module based on the New Tax Regime slabs under section 115BAC.
4. **Export Options:** Add 1-click PDF and CSV export for generated salary breakdown slips.
