from testclass import Test
import sample
import algo.arrays as dynarrays

test = Test()
test.test_prime(sample.is_prime)

da = dynarrays.DynamicArray()
test.test_array(da)