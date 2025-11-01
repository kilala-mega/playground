import unittest
from unittest.mock import patch
from io import StringIO
import contextlib

from hello import main, greet

class TestHelloMain(unittest.TestCase):
    def test_main_prints_greeting(self):
        with patch('builtins.input', return_value='Alice'):
            buf = StringIO()
            with contextlib.redirect_stdout(buf):
                main()
            self.assertEqual(buf.getvalue(), "Hello, Alice!\n")
    def test_greet(self):
        self.assertEqual(greet("Rumi"), "Hello, Rumi!")

if __name__ == "__main__":
    unittest.main()