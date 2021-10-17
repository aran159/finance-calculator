from finance_calculator import (
    PensionScheme,
    RegularInvestment
)


class TestRegularInvestment:
    def test_net_outcome(self):
        test_cases = [
            ({'A': 1000, 'R': 0, 't0': 0, 'Ta': 0}, 1000),
            ({'A': 1000, 'R': 0, 't0': 0.2, 'Ta': 0}, 800),
        ]

        for test_case_arguments, expected_result in test_cases:
            assert RegularInvestment(**test_case_arguments).net_outcome == expected_result
