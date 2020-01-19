"""
    Simple Merge Sort
"""
import random


class MergeSort:
    """
        This class implements Merge Sort
    """

    def __init__(self):
        pass

    def merge_sort(self, num_list):
        """
            implements simple recursive merge sort
        """
        # place holder for sorting
        num_list.sort()

        # add logic to perform merge sort
        return num_list


if __name__ == "__main__":
    list_nums = list(range(100))
    random.shuffle(list_nums)
    merge_sort_obj = MergeSort()
    sorted_list = merge_sort_obj.merge_sort(list_nums)
    print(sorted_list)
