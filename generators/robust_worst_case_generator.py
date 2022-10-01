import itertools

from helpers.list_helper import remove_list_duplicates
from variable import Variable


def get_robust_worst_test_cases(variables: list[Variable]):
    all_test_cases = list(itertools.product(*([variable.get_robust_values() for variable in variables])))

    return remove_list_duplicates(all_test_cases)
