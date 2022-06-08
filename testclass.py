import pytest

class Test:
    def test_prime(self, f):
        assert f(1) == False
        assert f(3) == True
        assert f("one") == False
        assert f(5) == True
        assert f(1000) == False
        assert f(13) == True

        print("\nTest cases for is_prime function passed!")
    # Note that we did not use pytest here. 
    # It was included for informational purposes.

    def test_array(self, arr):
        arr.append(5)
        arr.append(7)
        arr.append(10)
        assert len(arr) == 3
        assert arr[0] == 5
        assert arr[-1] == 10
        assert arr[1] == 7

        print("\nTest cases for dynamic arrays passed!")