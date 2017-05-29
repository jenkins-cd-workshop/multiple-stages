from unittest import TestCase

class MyTest(TestCase):
    def test_answer(self):
        answer = 42
        self.assertEqual(answer, 42);
