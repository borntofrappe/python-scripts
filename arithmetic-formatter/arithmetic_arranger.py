import re


def arithmetic_arranger(problems, show_solution=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    rows = {
        "first": [],
        "second": [],
        "third": []
    }
    output = ""

    for problem in problems:
        operand_1, operator, operand_2 = problem.split(" ")
        if operator == "*" or operator == "/":
            return "Error: Operator must be '+' or '-'."
        if re.search("\D", operand_1) or re.search("\D", operand_2):
            return "Error: Numbers must only contain digits."
        if len(operand_1) > 4 or len(operand_2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_len = max(len(operand_1), len(operand_2))
        row_width = max_len + 2

        row_first = operand_1.rjust(row_width, " ")
        row_second = operator + " " + operand_2.rjust(max_len, " ")
        row_third = "-" * row_width

        rows["first"].append(row_first)
        rows["second"].append(row_second)
        rows["third"].append(row_third)

        if show_solution:
            if "fourth" not in rows:
                rows["fourth"] = []
            num_1 = int(operand_1)
            num_2 = int(operand_2)
            solution = num_1
            if operator == "+":
                solution += num_2
            elif operator == "-":
                solution -= num_2

            row_fourth = str(solution).rjust(row_width, " ")
            rows["fourth"].append(row_fourth)

    spaces = 4
    column_spaces = " " * spaces
    rows_values = rows.values()
    for row in rows_values:
        output += column_spaces.join(row)
        output += "\n"

    return output[:-1]
