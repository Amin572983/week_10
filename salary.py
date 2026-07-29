"""
salary.py
Performs all salary calculations: overtime, service bonus,
gross salary, EPF, SOCSO and net salary.
"""

EPF_RATE = 0.11        # 11% EPF deduction
SOCSO_RATE = 0.005     # 0.5% SOCSO deduction
OVERTIME_RATE = 25     # RM25 per overtime hour (Activity 2.1)
LONG_SERVICE_BONUS = 200  # RM reward for employees with > 3 years service (Activity 2.2)
LONG_SERVICE_YEARS = 3


def calculate_overtime_pay(overtime_hours):
    """Return overtime pay based on RM25/hour."""
    return overtime_hours * OVERTIME_RATE


def calculate_long_service_bonus(years_of_service):
    """Return a reward bonus if employee has worked more than 3 years."""
    return LONG_SERVICE_BONUS if years_of_service > LONG_SERVICE_YEARS else 0


def calculate_gross_salary(basic_salary, allowance, overtime_hours=0, years_of_service=0):
    """Return total gross salary: basic + allowance + overtime pay + long service bonus."""
    overtime_pay = calculate_overtime_pay(overtime_hours)
    long_service_bonus = calculate_long_service_bonus(years_of_service)
    return basic_salary + allowance + overtime_pay + long_service_bonus


def calculate_epf(gross_salary):
    """Return EPF deduction = gross salary * 11%."""
    return gross_salary * EPF_RATE


def calculate_socso(gross_salary):
    """Return SOCSO deduction = gross salary * 0.5%."""
    return gross_salary * SOCSO_RATE


def calculate_net_salary(gross_salary):
    """Return net salary = gross salary - EPF - SOCSO."""
    return gross_salary - calculate_epf(gross_salary) - calculate_socso(gross_salary)