"""
employee.py
Collects employee information from the user.
"""


def get_employee():
    """Prompt the user for employee details and return them as a dict."""
    print("=== Employee Information ===")

    name = input("Employee Name : ")
    emp_id = input("Employee ID : ")
    basic_salary = float(input("Basic Salary (RM): "))
    allowance = float(input("Allowance (RM): "))

    # Activity 2.1 - HR now pays overtime (RM25/hour)
    overtime_hours = float(input("Overtime Hours: ") or 0)

    # Activity 2.2 - reward employees who worked more than 3 years
    years_of_service = float(input("Years of Service: ") or 0)

    employee = {
        "name": name,
        "id": emp_id,
        "basic_salary": basic_salary,
        "allowance": allowance,
        "overtime_hours": overtime_hours,
        "years_of_service": years_of_service,
    }

    return employee