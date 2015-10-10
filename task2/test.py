import subprocess
import unittest


class Task2Test(unittest.TestCase):
    def test_deduplicate(self):
        bash_command = 'cat task2/example-input.txt | ' \
                      './task2/input/mapper.py | sort -k1,1 | ./task2/input/reducer.py'
        output = subprocess.check_output(bash_command, shell=True)

        expected = subprocess.check_output('cat task2/example-output.txt', shell=True)
        self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()