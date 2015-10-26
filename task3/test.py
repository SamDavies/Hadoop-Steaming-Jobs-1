import subprocess
import unittest


class Task2Test(unittest.TestCase):
    def test_deduplicate(self):
        # given
        bash_command = 'cat task3/example-input.txt | ' \
                      './task3/input/mapper.py | sort -k1,1 | ./task3/input/combiner.py | ./task3/input/reducer.py'

        # when
        output = subprocess.check_output(bash_command, shell=True)

        # then
        self.assertEqual("21\t3\n", output)

if __name__ == '__main__':
    unittest.main()