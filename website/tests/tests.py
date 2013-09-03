from django import test


class SimpleTest(test.TestCase):

    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)
