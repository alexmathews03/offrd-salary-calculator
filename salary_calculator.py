"""
Offrd Product Engineering Intern Assignment - Part C Option 1
Salary Breakdown Calculator (Indian Payroll Compliance Rules)

Calculates monthly breakdown from Annual CTC:
- Basic Salary
- House Rent Allowance (HRA)
- Special Allowance (Balancing figure)
- Employer & Employee EPF
- Employer & Employee ESI (where applicable)
- Professional Tax
- Net Take-Home Salary
"""

from typing import Dict, Any


def calculate_monthly_salary(annual_ctc: float) -> Dict[str, Any]:
    """
    Takes an annual CTC and returns a detailed monthly payroll breakdown.

    Parameters:
        annual_ctc (float): Total annual Cost to Company in INR.

    Returns:
        dict: Breakdown containing monthly components, statutory deductions,
              and net take-home salary.
    """
    if annual_ctc <= 0:
        raise ValueError("Annual CTC must be a positive number greater than 0.")

    monthly_ctc = annual_ctc / 12.0

    # 1. Basic Salary: Configured as 50% of monthly CTC (standard Indian industry norm)
    basic = monthly_ctc * 0.50

    # 2. HRA: Configured as 50% of Basic Salary (Metro standard)
    hra = basic * 0.50

    # 3. EPF (Employee Provident Fund):
    # Statutory limit capped at Rs 15,000 basic wage per month.
    # Contribution: 12% of capped basic for both Employee and Employer.
    epf_wage_ceiling = 15000.0
    epf_base = min(basic, epf_wage_ceiling)
    employer_epf = epf_base * 0.12
    employee_epf = epf_base * 0.12

    # 4. ESI (Employee State Insurance):
    # Applicable ONLY if Gross Monthly Salary <= Rs 21,000.
    # Gross Salary estimate before ESI deduction = Monthly CTC - Employer EPF.
    estimated_gross = monthly_ctc - employer_epf

    if estimated_gross <= 21000.0:
        # Statutory ESI rates: 3.25% Employer, 0.75% Employee
        employer_esi = estimated_gross * 0.0325
        employee_esi = estimated_gross * 0.0075
    else:
        employer_esi = 0.0
        employee_esi = 0.0

    # 5. Gross Salary and Special Allowance:
    # Gross Salary is what the employee earns before employee-side deductions.
    gross_salary = monthly_ctc - employer_epf - employer_esi

    # Special allowance balances Basic + HRA with Gross Salary
    special_allowance = gross_salary - (basic + hra)

    # Edge Case: Extremely low CTC where Basic + HRA exceeds Gross Salary
    if special_allowance < 0:
        special_allowance = 0.0

    # 6. Professional Tax (PT):
    # Standard slab in most Indian states (e.g. Karnataka/Maharashtra/Telangana):
    # Rs 200/month if gross salary > Rs 15,000, else Rs 0.
    professional_tax = 200.0 if gross_salary > 15000.0 else 0.0

    # 7. Net Take-Home Salary:
    # Net Pay = Gross Salary - (Employee EPF + Employee ESI + Professional Tax)
    employee_deductions = employee_epf + employee_esi + professional_tax
    net_take_home = gross_salary - employee_deductions

    # Edge Case Guard: Ensure net take-home does not drop below zero
    if net_take_home < 0:
        net_take_home = 0.0

    return {
        "annual_ctc": round(annual_ctc, 2),
        "monthly_ctc": round(monthly_ctc, 2),
        "basic": round(basic, 2),
        "hra": round(hra, 2),
        "special_allowance": round(special_allowance, 2),
        "gross_salary": round(gross_salary, 2),
        "employer_epf": round(employer_epf, 2),
        "employee_epf": round(employee_epf, 2),
        "employer_esi": round(employer_esi, 2),
        "employee_esi": round(employee_esi, 2),
        "professional_tax": round(professional_tax, 2),
        "total_employee_deductions": round(employee_deductions, 2),
        "net_take_home": round(net_take_home, 2),
    }


def format_currency(val: float) -> str:
    """Helper to format currency as INR string."""
    return f"Rs {val:,.2f}"


def print_salary_slip(breakdown: Dict[str, Any]) -> None:
    """Pretty prints a salary breakdown for terminal/CLI usage."""
    print("=" * 60)
    print("          OFFRD - MONTHLY SALARY BREAKDOWN SLIP")
    print("=" * 60)
    print(f"Annual CTC:                     {format_currency(breakdown['annual_ctc'])}")
    print(f"Monthly CTC:                    {format_currency(breakdown['monthly_ctc'])}")
    print("-" * 60)
    print("EARNINGS:")
    print(f"  Basic Salary:                 {format_currency(breakdown['basic'])}")
    print(f"  House Rent Allowance (HRA):   {format_currency(breakdown['hra'])}")
    print(f"  Special Allowance:            {format_currency(breakdown['special_allowance'])}")
    print(f"  GROSS SALARY:                 {format_currency(breakdown['gross_salary'])}")
    print("-" * 60)
    print("EMPLOYER STATUTORY CONTRIBUTIONS (Part of CTC):")
    print(f"  Employer EPF (12%):           {format_currency(breakdown['employer_epf'])}")
    print(f"  Employer ESI (3.25%):         {format_currency(breakdown['employer_esi'])}")
    print("-" * 60)
    print("EMPLOYEE DEDUCTIONS (Subtracted from Gross):")
    print(f"  Employee EPF (12%):           {format_currency(breakdown['employee_epf'])}")
    print(f"  Employee ESI (0.75%):         {format_currency(breakdown['employee_esi'])}")
    print(f"  Professional Tax (PT):        {format_currency(breakdown['professional_tax'])}")
    print(f"  TOTAL EMPLOYEE DEDUCTIONS:    {format_currency(breakdown['total_employee_deductions'])}")
    print("=" * 60)
    print(f"  NET TAKE-HOME PAY:            {format_currency(breakdown['net_take_home'])}")
    print("=" * 60)


if __name__ == "__main__":
    import sys

    # Default to 6.0 LPA if no argument provided
    ctc_input = float(sys.argv[1]) if len(sys.argv) > 1 else 600000.0
    result = calculate_monthly_salary(ctc_input)
    print_salary_slip(result)
