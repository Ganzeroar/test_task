import task_2
import unittest
from task_2 import Data_type_not_valid
from task_2 import Invalid_parameter_value


class Test_total_cost_of_apartments(unittest.TestCase):

    def test_take_simple_data_return_correct_answer(self):
        obj = task_2
        result = obj.total_cost_of_apartments(3, 2, 1000)
        self.assertEqual(4000, result)

    def test_take_twice_increasing_cost_data_return_correct_answer(self):
        obj = task_2
        result = obj.total_cost_of_apartments(5, 2, 1000)
        self.assertEqual(9000, result)

    def test_take_real_data_return_correct_answer(self):
        obj = task_2
        result = obj.total_cost_of_apartments(30, 10, 10000)
        self.assertEqual(330000, result)

    def test_take_first_param_zero_return_exception(self):
        obj = task_2
        with self.assertRaises(Invalid_parameter_value) as context:
            obj.total_cost_of_apartments(0, 10, 10000)
        self.assertEqual(
            "Incorrect number_of_floors value: can't be zero value", str(context.exception))

    def test_take_second_param_zero_return_correct_answer(self):
        obj = task_2
        result = obj.total_cost_of_apartments(30, 0, 10000)
        self.assertEqual(300000, result)

    def test_take_third_param_zero_return_correct_answer(self):
        obj = task_2
        result = obj.total_cost_of_apartments(30, 10, 0)
        self.assertEqual(30000, result)

    def test_take_incorrect_first_param_return_exception(self):
        obj = task_2
        with self.assertRaises(Data_type_not_valid) as context:
            obj.total_cost_of_apartments('30', 10, 10000)
        self.assertEqual(
            "Incorrect number_of_floors type: <class 'str'>", str(context.exception))

    def test_take_incorrect_second_param_return_exception(self):
        obj = task_2
        with self.assertRaises(Data_type_not_valid) as context:
            obj.total_cost_of_apartments(30, '10', 10000)
        self.assertEqual(
            "Incorrect cost_increasing_floor type: <class 'str'>", str(context.exception))

    def test_take_incorrect_third_param_return_exception(self):
        obj = task_2
        with self.assertRaises(Data_type_not_valid) as context:
            obj.total_cost_of_apartments(30, 10, '10000')
        self.assertEqual(
            "Incorrect first_appartment_cost type: <class 'str'>", str(context.exception))


if __name__ == '__main__':
    unittest.main()
