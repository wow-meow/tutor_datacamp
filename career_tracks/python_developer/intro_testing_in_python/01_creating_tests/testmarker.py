#!/usr/bin/env python

import pytest
from datetime import datetime

day_of_week = datetime.now().isoweekday()
print(day_of_week)

def get_unique_values(lst):
    return list(set(lst))

condition_string = 'day_of_week == 6'
# Add the conditional skip marker and the string here

@pytest.mark.skipif(condition_string)
def test_function():
	# Complete the assertion tests here
    assert get_unique_values([1,2,3]) == [1,2,3]
    assert get_unique_values([1,2,3,1,7]) == [1,2,3,7]
