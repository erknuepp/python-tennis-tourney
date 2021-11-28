import player
import unittest

class Test_Player(unittest.TestCase):

    def test_initialize(self):
        expectedName = "Ed"
        expectedAge = 39
        expectedGender = "Male"
        expectedCountry = "US"
        expectedRating = 5.0
        actual = player.Player(expectedName, expectedAge, expectedGender, expectedCountry, expectedRating)
        self.assertEqual(expectedName, actual.name) 
        self.assertEqual(expectedAge, actual.age) 
        self.assertEqual(expectedGender, actual.gender) 
        self.assertEqual(expectedCountry, actual.country) 
        self.assertEqual(expectedRating, actual.rating) 