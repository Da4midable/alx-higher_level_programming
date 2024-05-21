#!/usr/bin/python3
if __name__ == "__main__":
    import unittest
    add_integer = __import__ ('0-add_integer').add_integer

    class TestMyFunc(unittest.TestCase):
        a, b = 10, 15
        result = a + b
        def test_add(self):
            
            self.assertEqual(add_integer(self.a, self.b), self.result)
            self.assertEqual(add_integer(10, -15), -5)
            self.assertEqual(add_integer(-10, -15), -25)
            self.assertEqual(add_integer(-10, 15), 5)
            
        def test_class(self):
            self.assertIsInstance(add_integer(self.a), (int, float))
            self.assertIsInstance(add_integer(self.b), (int, float))
            

  
if __name__ == '__main__':
    unittest.main()