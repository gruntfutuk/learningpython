# simple function to return payment on loan with compound interest
#
# main.py tab used for test code owing to limitations of repl.it
# repayment.py contains the function(s)
#
# add additional tests below as required

from repayments import glb
import unittest

class PaymentsTest(unittest.TestCase):

    def test_glb(self):
        self.assertEqual(round(glb(4773, 0.20),2), 442.14)
        self.assertEqual(round(glb(2012, 0.20),2), 186.38)
        self.assertEqual(round(glb(5443, 0.20),2), 504.21)

if __name__ == '__main__':
    unittest.main()