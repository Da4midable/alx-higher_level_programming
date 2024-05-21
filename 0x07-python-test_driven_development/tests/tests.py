#!/usr/bin/python3
if __name__ == "__main__":
    import unittest
    from add_integer import add_integer

    class TestMyFunc(unittest.TestCase):
        def test_add(self):
            result = add_integer(10, 15)
            self.assertEqual(result, 84)
    
if __name__ == '__main__':
    unittest.main()