# Salary Breakdown Calculator

Evaluation Exercise - Part C (Option 1) for Offrd Product Engineering Intern Assignment.

A Python module, command-line tool, and web interface that takes an annual Cost-to-Company (CTC) in INR and computes a detailed monthly payroll breakdown compliant with Indian statutory regulations.

---

## How to Run

### 1. Prerequisites
- Python 3.8 or higher installed on your machine.

Clone the repository and install dependencies:
```bash
git clone https://github.com/alexmathews03/offrd-salary-calculator.git
cd offrd-salary-calculator
pip install -r requirements.txt
```

### 2. Run the Web Interface (Recommended)
Start the local server:
```bash
python app.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000
```
Enter any annual CTC or use the preset buttons to view real-time recalculations of earnings, deductions, and take-home pay.

### 3. Run via Command Line (CLI)
You can calculate a breakdown directly from your terminal by passing an annual CTC amount:
```bash
python salary_calculator.py 600000
```
For low-salary testing (ESI eligible):
```bash
python salary_calculator.py 180000
```

### 4. Run the Unit Tests
Execute the automated test suite using pytest:
```bash
pytest test_calculator.py -v
```

---

## Assumptions

1. **Basic Salary:** Configured as 50% of monthly CTC, matching standard Indian compensation practices.
2. **House Rent Allowance (HRA):** Configured as 50% of Basic Salary (standard for metro locations).
3. **Employee Provident Fund (EPF):**
   - Statutory basic wage ceiling is capped at Rs 15,000 per month.
   - Contribution is 12% of the capped basic for both Employee and Employer (maximum contribution of Rs 1,800 per month each).
4. **Employee State Insurance (ESI):**
   - Applies only when Gross Monthly Salary is less than or equal to Rs 21,000 per month.
   - Employee Contribution: 0.75% of Gross Salary.
   - Employer Contribution: 3.25% of Gross Salary.
   - For gross salaries above Rs 21,000 per month, ESI is Rs 0.
5. **Special Allowance:** Serves as the balancing component ensuring Gross Salary equals Basic + HRA + Special Allowance.
6. **Professional Tax (PT):** Assumes standard state bracket of Rs 200 per month for gross salaries above Rs 15,000.

---

## Edge Cases Handled

1. **The ESI Threshold (Gross <= Rs 21,000/month):**
   - Handled dynamically: For lower CTCs (such as Rs 1.8 LPA), ESI deductions are automatically computed and subtracted. For higher salaries (such as Rs 6.0 LPA), ESI is automatically set to zero.
2. **The EPF Statutory Ceiling Cap:**
   - For higher salaries (such as Rs 24.0 LPA), EPF contributions do not escalate to 12% of full basic; they correctly cap at 12% of the Rs 15,000 ceiling (Rs 1,800/month).
3. **Low CTC Floor Guard:**
   - Prevents Special Allowance and net pay from evaluating to negative values on very low CTC entries.
4. **Input Validation:**
   - Raises a descriptive ValueError when an annual CTC is less than or equal to zero.

---

## Project Structure

```text
offrd-salary-calculator/
|-- app.py                 # Flask web server
|-- templates/
|   `-- index.html         # Web UI with real-time calculator
|-- salary_calculator.py   # Core payroll logic and CLI runner
|-- test_calculator.py     # Automated test suite (5 test cases)
|-- requirements.txt       # Dependencies (Flask, pytest)
|-- .gitignore             # Git ignore rules
`-- README.md              # Project documentation
```

---

## What I Would Do If I Had More Time

1. **Customizable Company Allowances:**
   Allow employers to configure custom allowance structures (such as Conveyance Allowance, Medical Allowance, or Performance Bonuses) instead of routing the entire balancing figure into Special Allowance.

2. **PDF and Excel Salary Slip Export:**
   Add a 1-click export feature allowing administrators to download a formatted PDF payslip or an Excel report of the salary breakdown ready for distribution to employees.
