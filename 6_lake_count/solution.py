import unittest
import os

# 探索の再帰関数
def solution(array_target):
    count_lake = 0
    return count_lake


def read_input(file_target):
    array_read = []
    with open(file_target) as f:
        text_list = f.readlines()
        text_list = [text.replace("\n", "") for text in text_list]
        for text in text_list:
            array_read.append(text.strip().split(" "))
    return array_read

class TestSolution(unittest.TestCase):
    def test_1_sample(self):
        array_read = read_input(f"{os.path.dirname(__file__)}/test.txt")
        self.assertEqual(array_read, 9)
    

if __name__ == "__main__":
    # array_read = read_input(f"{os.path.dirname(__file__)}/test.txt")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)