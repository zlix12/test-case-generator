# Test Case Generator

A simple project that generates test cases for methods. Currently, supports the generation of boundary value analysis
test cases.

# Usage

```python
from generators.nbv_case_generator import get_nbv_test_cases
from generators.robust_case_generator import get_robust_test_cases
from generators.robust_worst_case_generator import get_robust_worst_test_cases
from variable import Variable

if __name__ == '__main__':
    a = Variable("l", 1, 10)
    b = Variable("w", 1, 10)
    c = Variable("h", 1, 10)
    variables = [a, b, c]

    print("S1 = ", get_nbv_test_cases(variables))
    print("S2 = ", get_robust_test_cases(variables))
    print("S3 = ", get_robust_worst_test_cases(variables))
```