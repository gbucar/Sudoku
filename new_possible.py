def row_to_column(row):
    column = [[] for i in range(3)]
    for r in row:
        for ii, char in enumerate(r):
            column[ii].append(char)
    return column

def create_base_three():
    line = [i for i in range(3)]
    base = []
    for a in range(3):
        base.append(create_order_row(line))
        line = reorder(line)
    return base

def create_order_row(line):
    return [line for i in range(3)]

def reorder(lis):
    return [lis[-1]]+lis[:-1]

def create_options_from_base(base):
    options = []
    for i in range(3):
        current = list(base)
        for ii in range(2):
            current[i] = reorder(current[i])
            options.append(list(current))
    return options + [base]

def create_rows():
    base_three = create_base_three()
    all = []
    for base in base_three:
        all += create_options_from_base(base)
    return all

def create_columns():
    return [row_to_column(i) for i in create_rows()]

options = open("options.txt", "w")
options.write(str(create_rows()))
options.write("\n")
options.write(str(create_columns()))
options.close()