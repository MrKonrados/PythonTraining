"""
Background
    In a set of numbers, the mean is the average, the mode is the number that occurs the most, and if you rearrange all 
    the numbers numerically, the median is the number in the middle.

Goal
    Create three functions that allow the user to find the mean, median, and mode of a list of numbers. If you have 
    access or know of functions that already complete these tasks, do not use them.

Subgoals
    - In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
    - If there is an even number of numbers in the list, return both numbers that could be considered the median.
    - If there are multiple modes, return all of them.
"""
import operator

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# numbers = [5,1,2,4,3,45,12,44,0,13,9,8]
# numbers = [1,2,3,4,5,6]

def mean(list):
    return sum(list) / len(list)


def mode(list):
    d = dict()
    for numer in list:
        d[numer] = list.count(numer)
    return sorted(d.items(), key=operator.itemgetter(1), reverse=True)[0][0]


def median(list):
    list = sorted(list)
    # print(list, 'len=',len(list))
    if len(list) % 2:
        return list[int(len(list)/2)]
    else:
        return [list[int(len(list)/2)-1], list[int(len(list)/2)]]

print('srednia: ', mean(numbers))
print('dominanta: ', mode(numbers))
print('median: ', median(numbers))