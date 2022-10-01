from helpers.list_helper import remove_list_duplicates
from variable import Variable


def get_robust_test_cases(variables: list[Variable]):
    all_test_cases = []
    for var_index, variable in enumerate(variables):
        for value_index, value in enumerate(variable.get_robust_values()):
            case = [other_var.get_nominal_value() for other_var in variables[0:var_index] if other_var != variable] + \
                   [value] + \
                   [other_var.get_nominal_value() for other_var in variables[var_index:len(variables)] if other_var != variable]
            all_test_cases.append(tuple(case))

    return remove_list_duplicates(all_test_cases)