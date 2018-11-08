import unittest
import numpy as np
import re


def simple_adder(a, b):
    return a + b


def insert_if_not_in_dict(dict, key, value):
    if key in dict:
        return False
    else:
        dict[key] = value
        return True


my_dict = {"1": 1, "2": 2}


def random_list(size):
    return np.random.randint(10, size=size)


def is_date_in_string(string):
    words = string.split(' ')
    data_markers = ['год', 'г', 'век', 'месяц', 'лет', 'эры', 'март', 'мае']
    for word in words:
        if re.match(r"^[0-9]{4}$", word):
            return True
        for marker in data_markers:
            if marker in word:
                return True
    return False


class SimpleTester(unittest.TestCase):

    # Each test is written as a method with a name beginning with "test_"
    def test_return_value(self):
        self.assertEqual(simple_adder(-2, 7), 5)
        # bad idea to check value in dict
        self.assertTrue(insert_if_not_in_dict(my_dict, "4", 4))
        self.assertFalse(insert_if_not_in_dict(my_dict, "4", 4))
        self.assertGreater(simple_adder(4, 5), 4)
        self.assertLess(simple_adder(-2, -4), -2)

    def test_existance(self):
        insert_if_not_in_dict(my_dict, "6", 6)
        self.assertIn("6", my_dict)
        self.assertNotIn("5", my_dict)
        my_list = ["1", "2", "6"]
        self.assertCountEqual(my_dict, my_list)

    def test_date(self):
        # string = input()
        test_cases = ['с тех пор прошло 3 года', 'бюджет в 2018 году'
            , 'в 6 веке'
            , '5 марта'
            , 'почти половина мужчин не доживают до 65 лет'
            , 'в 1897 г'
            , '1978 до нашей эры'
            , 'в мае 2018 года']
        for test in test_cases:
            self.assertTrue(is_date_in_string(test))

    def test_list(self):
        size = int(input())
        test_list = random_list(size)
        for value in test_list:
            self.assertGreater(value,0.5)
