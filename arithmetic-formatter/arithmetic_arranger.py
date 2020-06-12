def arithmetic_arranger(problems):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        # list in which to store the different operations, through nested list describing the lines
        arrangements = []
        for problem in problems:
            # the numbers and the operator are handily separated by a white space
            split = problem.split(' ')
            num_1 = split[0]
            operator = split[1]
            num_2 = split[2]

            # i'm positive there's a better way to handle different conditionals
            if operator == '+' or operator == '-':
                if num_1.isnumeric() and num_2.isnumeric():
                    if len(num_1) <= 4 and len(num_2) <= 4:
                        # include the three lines in a list
                        length = max([len(num_1), len(num_2)]) + 2
                        arrangement = [
                            num_1.rjust(length, " "),
                            operator + num_2.rjust(length - 1, " "),
                            '-'*length
                        ]
                        arrangements.append(arrangement)
                    else:
                        return('Error: Numbers cannot be more than four digits.')
                else:
                    return('Error: Numbers must only contain digits.')
            else:
                return('Error: Operator must be \'+\' or \'-\'.')

        # still unsure as the best way to concatenate the nested strings
        arranged_problems = ''
        for i in list(range(len(arrangements[0]))):
            for j in list(range(len(arrangements))):
                arranged_problems += arrangements[j][i]
                if(j < len(arrangements) - 1):
                    arranged_problems += ' '*4
            if(i < len(arrangements[0]) - 1):
                arranged_problems += '\n'

        return arranged_problems
