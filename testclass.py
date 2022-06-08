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

    def test_anagram(self, ana):
        s1 = "God"
        s2 = 'dog'
        s3 = 'Clint Eastwood'
        s4 = 'Old West Action'
        s5 = 'Lagos'
        s6 = 'goals'
        s7 = 'Public Relations'
        s8 = 'crap built on lies'

        assert ana(s1, s2) == True
        assert ana(s1, s3) == False
        assert ana(s5, s6) == True
        assert ana(s4, s5) == False
        assert ana(s7, s8) == True
        assert ana(s3, s4) == True

        print("\nTest cases for anagram passed!")

    def test_array_pair(self, ap):
        assert ap([1, 3, 2, 2, 1, 0, 4, 4, 0], 4) == {(1, 3), (0, 4), (2, 2)}
        assert ap([1, 3, 2, 2, 1, 0, 4, 4], 4) == {(1, 3), (0, 4), (2, 2)}
        assert ap([1, 3, 2, 2, 1], 4) == {(1, 3), (2, 2)}

        print("\nTest cases for array pair passed!")