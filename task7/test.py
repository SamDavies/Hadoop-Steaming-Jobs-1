import subprocess
import unittest


class Task7Test(unittest.TestCase):
    def test_matrix(self):
        # given
        bash_command = 'cat task7/example-input.txt | ' \
                       './task7/input/mapper.py | sort -nk1,1 | ./task7/input/reducer.py'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = subprocess.check_output('cat task7/example-output.txt', shell=True)

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
