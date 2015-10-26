import subprocess
import unittest


class Task9Test(unittest.TestCase):
    def test_both(self):
        # given
        bash_command = 'cat task9/example-mapper-input.txt | ' \
                       './task9/input/mapper.py | sort -nk1,1 | ./task9/input/reducer.py'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = subprocess.check_output('cat task9/example-reducer-output.txt', shell=True)

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
