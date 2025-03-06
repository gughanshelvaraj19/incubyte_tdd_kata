import pytest

from string_calculator import add


class TestAdd:

    def test_invalid_seq(self):
        assert add("") == 0
        assert add(" ") == 0
        assert add(",") == 0
        assert add("A, B") == 0
        assert add(1) == 0
        assert add((1,)) == 0
        assert add([1, 2]) == 0

    def test_single_digit_seq(self):
        assert add("1,2,3") == 6
        assert add("1,2,3,") == 6
        assert add("1,2,3,1*1") == 8
        assert add("1,2,3,1*1,") == 8
        assert add("1,2,3,1*1,B,A(10") == 18
        assert add("1,2,3,1*1,B,A(10)_") == 18

    def test_single_digit_seq_special(self):
        assert add("\\1,2,3,1*1,\nB,A(10\n") == 18
        assert add("1,2\n3!") == 6

    def test_multi_digit_seq(self):
        assert add("1,2,3,10*10") == 26
        assert add("1,2,3,10*10,") == 26
        assert add("1,1,1,000*0001}0001*1000+1+1,") == 1007
        assert add("1,1,1,000*0001}0001*1000+1+1\n") == 1007

    def test_single_digit_large_seq(self):
        assert add("1,1,1,000*0001}0001*1000+1+1," * 100000) == 100700000
        assert add("1,1,1,000*0001}0001*1000+1+1," * 1000000) == 1007000000
        assert add("1,1,1,000*0001}0001*1000+1+1," * 10000000) == 10070000000
        assert add("1,1,1,000*0001}0001*1000+1+1," * 100000000) == 100700000000
