import pytest

class Test(object):
    def test_prime(self, f):
        assert f(1) == False
        assert f(3) == True
        assert f("one") == False
        assert f(5) == True
        assert f(1000) == False
        assert f(13) == True

        print("Test cases passed!")
    # Note that we did not use pytest here. 
    # It was included for informational purposes.

    def test_array(self, f):
        pass