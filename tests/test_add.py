import pytest

from string_calculator import add


class TestAdd:

    def test_basecase(self):
        assert add("") == 0
        assert add(" ") == 0
        assert add(",") == 0
        assert add("A, B") == 0
        assert add(1) == 0
        assert add((1,)) == 0
        assert add([1, 2]) == 0

    def test_inputcase(self):
        assert add("1,2,3") == 6
        assert add("1,2,3,") == 6
        assert add("1,2,3,1*1") == 8
