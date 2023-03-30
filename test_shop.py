import unittest
from unittest import mock
from unittest.mock import patch
from shop import purchase_item, shop, NotEnoughMoneyError, MaxPurchaseAttemptsExceededError

class TestShop(unittest.TestCase):
    def test_purchase_item_valid(self):
        available_money = 100
        expected_money_left = 50
        actual_money_left = purchase_item("pen", available_money)
        self.assertEqual(actual_money_left, expected_money_left)

    def test_purchase_item_invalid(self):
        available_money = 100
        with self.assertRaises(ValueError):
            purchase_item("pencil", available_money)

    def test_purchase_item_not_enough_money(self):
        available_money = 50
        with self.assertRaises(NotEnoughMoneyError):
            purchase_item("backpack", available_money)

    def test_shop_valid_additional_money(self):
        with patch('builtins.input', side_effect=['notebook', 'yes', '100', 'notebook','exit']):
            with patch('builtins.print') as mocked_print:
                shop()
                mocked_print.assert_any_call("You don't have enough money to purchase this item")
                mocked_print.assert_any_call("You now have £200")
                mocked_print.assert_any_call("Here's your notebook!")
                mocked_print.assert_any_call("You have £50 left")

    def test_shop_valid_purchase(self):
        with patch('builtins.input', side_effect=['pen', 'exit']):
            with patch('builtins.print') as mocked_print:
                shop()
                mocked_print.assert_any_call("Here's your pen!")
                mocked_print.assert_any_call("You have £50 left")


if __name__ == '__main__':
    unittest.main()
