from lib.day_1 import *

"""
From adventofcode.com:
> On each line, the calibration value can be found by
> combining the first digit and the last digit (in that order)
> to form a single two-digit number.
"""
def test_single_line_parses_correctly():
    test_cases = [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ]
    for line, expected in test_cases:
        assert parse_single_line(line) == expected

"""
From adventofcode.com:
> Consider your entire calibration document.
> What is the sum of all of the calibration values?
"""

def test_calibration_document_parses_correctly():
    document = "\n".join((
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ))
    assert parse_document(document) == 142
