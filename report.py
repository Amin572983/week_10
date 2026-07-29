"""
report.py
Displays the final salary report to the user.
"""


def print_report(name, employee_id, gross_salary, epf, socso, net_salary,
                  overtime_hours=0, years_of_service=0):
    """Print a formatted salary report for the given employee."""
    print("========== SALARY REPORT ==========")
    print(f"Employee Name : {name}")
    print(f"Employee ID  : {employee_id}")

    if overtime_hours > 0:
        print(f"Overtime Hours: {overtime_hours}")
    if years_of_service > 3:
        print("Long Service Bonus : Awarded (worked > 3 years)")

    print()
    print(f"Gross Salary : RM {gross_salary:.2f}")
    print(f"EPF (11%)    : RM {epf:.2f}")
    print(f"SOCSO (0.5%) : RM {socso:.2f}")
    print()
    print(f"Net Salary   : RM {net_salary:.2f}")
    print("====================================")