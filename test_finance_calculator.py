import pytest
from finance_calculator import (
    PensionScheme,
    RegularInvestment
)


class TestRegularInvestment:
    @pytest.mark.parametrize(
        'test_input,expected', 
        [
            ({'A': 1000, 'R': 0, 't0': 0, 'Ta': 0}, 1000),
            ({'A': 1000, 'R': 0, 't0': 0.2, 'Ta': 0}, 800),
            ({'A': 1000, 'R': 0.1, 't0': 0, 'Ta': 0}, 1100),
            ({'A': 1000, 'R': 1.0, 't0': 0.2, 'Ta': 0}, 1600),
            ({'A': 1000, 'R': 0, 't0': 0, 'Ta': 0.2}, 1000),
            ({'A': 1000, 'R': 1, 't0': 0, 'Ta': 0.5}, 1500),
            ({'A': 1000, 'R': 0.1, 't0': 0.9, 'Ta': 0.5}, 105),
        ]
    )
    def test_net_outcome(self, test_input, expected):
        assert pytest.approx(RegularInvestment(**test_input).net_outcome) == expected
