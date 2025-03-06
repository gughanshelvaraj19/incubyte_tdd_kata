import pytest
from string_calculator import ondemand_char_gettr


class TestOnDemandCharGettr:
    def test_ondemand_char_gettr(self):
        test_case1 = "1,2,3"
        assert [number for number in ondemand_char_gettr(test_case1)] == [1, 2, 3]
