"""
main.py
Coordinates the salary calculator workflow:
1. Collect employee details (employee.py)
2. Calculate salary figures (salary.py)
3. Display the salary report (report.py)
"""

from employee import get_employee
from salary import (
    calculate_gross_salary,
    calculate_epf,
    calculate_socso,
    calculate_net_salary,
)
from report import print_report


def main():
    employee = get_employee()

    gross_salary = calculate_gross_salary(
        employee["basic_salary"],
        employee["allowance"],
        employee["overtime_hours"],
        employee["years_of_service"],
    )
    epf = calculate_epf(gross_salary)
    socso = calculate_socso(gross_salary)
    net_salary = calculate_net_salary(gross_salary)

    print_report(
        employee["name"],
        employee["id"],
        gross_salary,
        epf,
        socso,
        net_salary,
        employee["overtime_hours"],
        employee["years_of_service"],
    )


if __name__ == "__main__":
    main()