import unittest
import os, copy

# 探索の再帰関数
def solution(array_target):
    count_lake = 0
    array_count = copy.deepcopy(array_target)

    return count_lake

def find_neighbor(array_target, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if row + i < 0 or row + i >= len(array_target):
                continue
            if col + j < 0 or col + j >= len(array_target[0]):
                continue
            if array_target[row + i][col + j] == 1:
                count += 1
    return count

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
    array_read = read_input(f"{os.path.dirname(__file__)}/test.txt")
    solution(array_read)
    # unittest.main(argv=['first-arg-is-ignored'], exit=False)