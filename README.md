# week_10
# Week 10 - Salary Calculator

A simple modular Python salary calculator built for an HR software company.
The HR department currently calculates employees' monthly salaries manually —
this program automates the process.

## Features

- Collects employee information (name, ID, basic salary, allowance)
- Calculates gross salary
- Calculates EPF deduction (11%)
- Calculates SOCSO deduction (0.5%)
- Calculates net salary
- Displays a salary summary / report
- **Overtime pay**: overtime is paid at RM25/hour and added to gross salary
- **Long service bonus**: employees with more than 3 years of service receive
  an RM200 reward, added to gross salary

## Project Structure

```
week_10/
├── main.py       # Coordinates the overall workflow
├── employee.py   # Collects employee details from the user
├── salary.py     # Performs all salary calculations
├── report.py     # Displays the final salary report
└── README.md     # Project documentation
```

## How It Works

1. `main.py` calls `get_employee()` from `employee.py` to collect employee
   details, including basic salary, allowance, overtime hours, and years of
   service.
2. `main.py` passes those details to the calculation functions in
   `salary.py`:
   - `calculate_gross_salary()` — basic salary + allowance + overtime pay
     + long service bonus (if applicable)
   - `calculate_epf()` — 11% of gross salary
   - `calculate_socso()` — 0.5% of gross salary
   - `calculate_net_salary()` — gross salary minus EPF and SOCSO
3. `main.py` passes all the calculated figures to `display_report()` in
   `report.py`, which prints a formatted salary report.

## Usage

```bash
python3 main.py
```

You will be prompted to enter:

- Employee Name
- Employee ID
- Basic Salary (RM)
- Allowance (RM)
- Overtime Hours (press Enter for 0)
- Years of Service (press Enter for 0)

### Example

```
=== Employee Information ===
Employee Name : Ali
Employee ID : EMP001
Basic Salary (RM): 3500
Allowance (RM): 400
Overtime Hours: 0
Years of Service: 0

======== SALARY REPORT ========
Employee Name : Ali
Employee ID  : EMP001
----------------------------
Gross Salary : RM 3900.00
EPF (11%)    : RM 429.00
SOCSO (0.5%) : RM 19.50
----------------------------
Net Salary   : RM 3451.50
============================
```

## Business Rules

| Item                | Rule                                              |
|---------------------|----------------------------------------------------|
| EPF                 | 11% of gross salary                               |
| SOCSO               | 0.5% of gross salary                              |
| Overtime Pay        | RM25 per overtime hour                            |
| Long Service Bonus  | RM200, awarded if years of service > 3            |
| Net Salary          | Gross salary − EPF − SOCSO                        |

> Note: The overtime rate and long service bonus amount are configurable
> constants at the top of `salary.py` (`OVERTIME_RATE` and
> `LONG_SERVICE_BONUS`) so the HR department can adjust them easily.