import subprocess
import unittest


class Task6Test(unittest.TestCase):
    def test_top_20(self):
        # given
        bash_command = 'cat task6/example-input.txt | ' \
                       './task6/input/mapper.py | sort -nrk1,1 | ./task6/input/combiner.py | ./task6/input/reducer.py'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = subprocess.check_output('cat task6/example-output.txt', shell=True)

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
