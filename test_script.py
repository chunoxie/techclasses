from testclass import Test
import sample
import algo.arrays as dynarrays
import algo.anagram as anagram

test = Test()

test.test_prime(sample.is_prime)

test.test_array(dynarrays.DynamicArray())

test.test_anagram(anagram.anagram_simple)

test.test_anagram(anagram.anagram_optimal)