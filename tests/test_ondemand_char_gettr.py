import pytest

from string_calculator import ondemand_char_gettr


class TestOnDemandCharGettr:
    def test_single_digit_seq(self):
        """
        Tests single-digit sequence
        """
        test_case1 = "1,2,3"
        assert [number for number in ondemand_char_gettr(test_case1)] == [1, 2, 3]
        test_case1 = "1*2-3,4"
        assert [number for number in ondemand_char_gettr(test_case1)] == [1, 2, 3, 4]

    def test_multi_digit_seq(self):
        """
        Tests multi-digit sequence
        """
        test_case1 = "1,12,3,45"
        assert [number for number in ondemand_char_gettr(test_case1)] == [1, 12, 3, 45]

        test_case1 = "1,12\n3,45\t1000\v000"
        assert [number for number in ondemand_char_gettr(test_case1)] == [
            1,
            12,
            3,
            45,
            1000,
            0,
        ]
        test_case1 = "1,12\n3,45\t1003\v000"
        assert [number for number in ondemand_char_gettr(test_case1)] == [
            1,
            12,
            3,
            45,
            0,
        ]
