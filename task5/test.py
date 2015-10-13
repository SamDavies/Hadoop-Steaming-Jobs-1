import subprocess
import unittest


class Task2Test(unittest.TestCase):
    def test_deduplicate(self):
        # given
        bash_command = 'cat task5/example-input.txt | ' \
                       './task5/input/mapper.py | sort -k1,1 | ./task5/input/reducer.py'
        output = subprocess.check_output(bash_command, shell=True)

        # when
        expected = 'a lamb\t1\n' \
                   'a tiger\t1\n' \
                   'had a\t3\n' \
                   'lamb had\t1\n' \
                   'mary had\t2\n'

        # then
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
