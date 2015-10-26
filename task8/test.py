import subprocess
import unittest


class Task8Test(unittest.TestCase):
    def test_mapper(self):
        # given
        bash_command = 'cat task8/example-mapper-input.txt | ' \
                       './task8/input/mapper.py | sort -nk1,1'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = subprocess.check_output('cat task8/example-mapper-output.txt', shell=True)

        # then
        self.assertEqual(expected, output)

    def test_reducer(self):
        # given
        bash_command = 'cat task8/example-mapper-input.txt | ' \
                       './task8/input/mapper.py | sort -nk1,1 | ./task8/input/reducer.py'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = subprocess.check_output('cat task8/example-reducer-output.txt', shell=True)

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
