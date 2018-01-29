from __future__ import division
import numpy as np
class TestClass(object):
    def test_one(self):
        x = 2
        y = 8
        assert x / float(8) == 0.25

    def test_two(self):
        assert np.true_divide([2],[8]) == 0.25