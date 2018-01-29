import numpy as np
class TestClass(object):
    def test_one(self):
        x = 2
        y = 8
        assert x / y == 0.25

    def test_two(self):
        assert np.true_divide([2],[8])