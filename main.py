def arithmetic_arranger(problems, solve=False):
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''

    accepted = ['+', '-']
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        o1, s, o2 = problem.split()
        le = max([o1, o2], key=len)
        if s not in accepted:
            return "Error: Operator must be '+' or '-'."
        elif not o1.isnumeric() or not o2.isnumeric():
            return "Error: Numbers must only contain digits."
        elif len(le) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            if problems.index(problem) != (len(problems) - 1):
                r1 += (o1.rjust(len(le) + 2) + '    ')
                r2 += (s + (o2.rjust(len(le) + 1)) + '    ')
                r3 += ('-' * (len(le) + 2) + '    ')
                if s == '+':
                    r4 += (str(int(o1) + int(o2)).rjust(len(le) + 2) + '    ')
                else:
                    r4 += (str(int(o1) - int(o2)).rjust(len(le) + 2) + '    ')
            else:
                r1 += (o1.rjust(len(le) + 2))
                r2 += (s + (o2.rjust(len(le) + 1)))
                r3 += ('-' * (len(le) + 2))
                if s == '+':
                    r4 += (str(int(o1) + int(o2)).rjust(len(le) + 2))
                else:
                    r4 += (str(int(o1) - int(o2)).rjust(len(le) + 2))

    if solve:
        r1 += '\n'
        r2 += '\n'
        r3 += '\n'
        arranged_problems = r1 + r2 + r3 + r4
    else:
        r1 += '\n'
        r2 += '\n'
        arranged_problems = r1 + r2 + r3

    return arranged_problems
