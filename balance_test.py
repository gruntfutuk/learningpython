import unittest


def balance(alpha, beta):
    "return string of whichever is longer of <alpha> or <beta>"
    "that constitutes the substring of the longer part"
    "(return empty string if same length)"
    len_alpha = len(alpha)
    len_beta = len(beta)
    if len_alpha < len_beta:
        return beta[len_alpha:]
    elif len_beta < len_alpha:
        return alpha[len_beta:]
    else:
        return ""


class TestBalance(unittest.TestCase):
    def test_balance(self):
        self.assertEqual(balance("aaaa", "b"), "aaa", "Should be aaa")


unittest.main()
