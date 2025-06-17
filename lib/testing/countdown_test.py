import io
import sys
import pytest
from lib.countdown import countdown  # <-- ✅ this is the important line

class TestCountdown:
    def test_counts_down_prints_happy_new_year(self):
        '''counts down from number and prints "HAPPY NEW YEAR!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        countdown(5)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "5 SECOND(S)!\n4 SECOND(S)!\n" + \
               "3 SECOND(S)!\n2 SECOND(S)!\n1 SECOND(S)!\nHAPPY NEW YEAR!\n")
