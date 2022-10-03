def arithmetic_arranger(problems, answer=False):
    # Check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    num1 = []
    num2 = []
    operator = []
    for problem in problems:
        problem = problem.split()
        num1.append(problem[0])
        operator.append(problem[1])
        num2.append(problem[2])

    # Checks for other possible operators
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    # Checks if all values/elements are digits
    if not (all(i.isdigit() for i in num1) and all(j.isdigit() for j in num2)):
        return "Error: Numbers must only contain digits."

    # Checks the lenghts of the numbers
    if not (all(len(x) <= 4 for x in num1) and all(len(y) <= 4 for y in num2)):
        return "Error: Numbers cannot be more than four digits."
    
    # Formatting process
    line1 = []
    line2 = []
    dash = []
    result = []

    # Appends each value with their corresponding string lenght
    for a in range(len(num1)):
        if len(num1[a]) == len(num2[a]):
            line1.append(" "*2 + num1[a])
            line2.append(operator[a] + " " + num2[a])
            dash.append("-" * (len(line1[a])))
        elif len(num1[a]) > len(num2[a]):
            line1.append(" "*2 + num1[a])
            line2.append(operator[a] + " "*((len(line1[a]) - len(num2[a])) - 1) + num2[a])
            dash.append("-" * len(line1[a]))
        else:
            line1.append(" "*(len(num2[a]) - len(num1[a]) + 2) + num1[a])
            line2.append(operator[a] + " " + num2[a])
            dash.append("-"*(len(line1[a])))

    # Computes for the specified operation of the problem
    for a in range(len(num1)):
        m = int(num1[a]) + int(num2[a]) if operator[a] == "+" else int(num1[a]) - int(num2[a])
        result.append(" "*(len(dash[a]) - len(str(m))) + str(m))
    
    # Checks if answer is set to True or False and returns the corresponding format
    if answer:
        arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(dash) + "\n" + "    ".join(result)
    else:
        arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(dash)
    
    
    return arranged_problems
