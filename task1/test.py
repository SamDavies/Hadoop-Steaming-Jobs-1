import subprocess
import unittest


class TestTask1(unittest.TestCase):
    def test_to_lower(self):
        bash_command = 'cat task1/example-input.txt | ' \
                      './task1/input/mapper.py | ./task1/input/reducer.py'
        output = subprocess.check_output(bash_command, shell=True)

        expected = subprocess.check_output('cat task1/example-output.txt', shell=True)
        self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()