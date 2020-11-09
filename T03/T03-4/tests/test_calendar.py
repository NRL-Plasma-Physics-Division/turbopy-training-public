import sys
import pytest

sys.path.append('./')  # sets to the directory before test/
from date import Date
from datetime import datetime
from datetime import date as d


@pytest.fixture
def date():
    """Creates fixture for today's date"""
    return Date(str(datetime.date(datetime.now()))[5:] + ' 2020')


@pytest.fixture
def invalid():
    """Creates fixture with an invalid date"""
    return Date('02 29 2019')


def test_sub(date):
    """Tests whether the build-in sub method works for Date objects"""
    tester = Date('07 04 2020')
    assert tester
    assert date
    assert date - tester > 0
    assert date - tester == (datetime.date(datetime.now()) - d(2020, 7, 4)).days


def test_string():
    """Tests whether or not the datetime.date() method returns a str"""
    assert not isinstance(datetime.date(datetime.now()), str)


def test_invalid(date, invalid):
    """Tests whehter or not the sub method returns -1 if one date is invalid"""
    assert invalid - date == -1
