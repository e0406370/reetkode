"""
LCE 2879. Display the First Three Rows

DataFrame: employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+

Write a solution to display the first 3 rows of this DataFrame.
"""


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:

    # alt: return employees[:3]
    return employees.head(3)
