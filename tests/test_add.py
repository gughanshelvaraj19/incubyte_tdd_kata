import pytest

from string_calculator import add, NegativeNumberException


class TestAdd:

    def test_invalid_seq(self):
        """
        Tests possible invalid sequences and sequence-types.
        """
        assert add("") == 0
        assert add(" ") == 0
        assert add(",") == 0
        assert add(",!{},,!") == 0
        assert add("A, B") == 0
        assert add(1) == 0
        assert add((1,)) == 0
        assert (
            add(
                (
                    1,
                    2,
                )
            )
            == 0
        )

    def test_single_digit_seq(self):
        """
        Tests single-digit sequence with various delimiters.
        """
        assert add("1,2,3") == 6
        assert add("1,2,3,") == 6
        assert add("1,2,3,1*1") == 8
        assert add("1,2,3,1*1,") == 8
        assert add("1,2,3,1*1,B,A(10") == 18
        assert add("1,2,3,1*1,B,A(10)_") == 18

    def test_single_digit_seq_special(self):
        """
        Tests single-digit sequence with special characters such as \n,\t,\\,etc.
        """
        assert add("\\1,2,3,1*1,\nB,A(10\n") == 18
        assert add("1,2\n3!") == 6
        assert add("\t1,2\n3!\t\\") == 6

    def test_multi_digit_seq(self):
        """
        Tests multi-digit sequence with various delimiters.
        """
        assert add("1,2,3,10*10") == 26
        assert add("1,2,3,10*10,") == 26
        assert add("1,1,1,000*0001}0001*1000+1+1,") == 1007

    def test_multi_digit_seq_special(self):
        """
        Tests multi-digit sequence with special characters such as \n,\t,\\,etc.
        """
        assert add("1,1,1,000*0001}\n0001\n*1000+1+1\n") == 1007
        assert add("\n1,1,1,000*0001}\n0001\n*1000+1+1\n") == 1007

    def test_multi_digit_seq_with_1000_more(self):
        """
        Tests multi-digit sequence with 1000s and more values added
        """
        assert add("1,1,1,000*0001}\n0001\n*100000+1+1\n") == 7
        assert add("\n1,1,1,000*0001}\n00010002\n*1000+1+1\n") == 1006

    def test_seq_with_negatives(self):
        """
        Tests multi-digit sequence with negatives
        """
        assert (
            add("1,1,1,000*0001}\n0001\n*1000+1+1-154-1\n", raise_exception=False)
            == 1007
        )
        assert (
            add("\n1,1,1,000*0001}\n0001\n*1000+1+1-145-1\n", raise_exception=False)
            == 1007
        )
        assert (
            add("1,1,1,000*0001}0001*1000+1+1,&&-456--", raise_exception=False) == 1007
        )
        assert add("1,2,3,10*10,\n-1-456&&-34567--", raise_exception=False) == 26
        assert add("1,2,3,10*10-456-5", raise_exception=False) == 26
        assert add("-1,-2,3,10*10-456-5", raise_exception=False) == 23
        assert add("-1,-2,-3,10*10)456(5\n", raise_exception=False) == 481
        assert add("-1,-2,-3,-10*-10)-456-(-5\n", raise_exception=False) == 0

    def test_seq_with_negatives_raises_exception(self):
        """
        Tests multi-digit sequence with negatives
        """
        with pytest.raises(NegativeNumberException):
            add("1,1,1,000*0001}\n0001\n*1000+1+1-154-1\n")

        with pytest.raises(
            NegativeNumberException,
            match="Negative numbers not allowed <-1,-2,-3,-10,-10,-456,-5,>",
        ):
            add("-1,-2,-3,-10*-10)-456-(-5\n")


class TestLargeDataset:
    def test_large_seq(self):
        """
        Tests large sequences with various delimiters and special characters.
        """
        assert add("1,1,1,000*0001}0001*1000+1+1," * 100000) == 100700000
        # assert add("1,1,1,000*0001}0001*1000+1+1," * 1000000) == 1007000000
        # assert add("1,1,1,000*00\\01}\\0001*1000\n+1+1," * 1000000) == 1007000000
        # assert add("-342/-1**\n1,1,1,000*0001}0001*1000+1+1-1," * 100000) == 100700000

        # assert add("1,1,1,000*0001}0001*1000+1+1," * 10000000) == 10070000000
        # assert add("1,1,1,000*0001}0001*1000+1+1," * 100000000) == 100700000000
