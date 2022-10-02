"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def calc_median(nums):
    odd = True if len(nums) % 2 == 1 else False
    if odd:
        median = nums[int( len(nums) / 2 )]
    else:
        median = (nums[int( len(nums) / 2 )] + nums[int( len(nums) / 2  )- 1]) / 2

    return median

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
# print(numbers)
# print(f'{calc_median(numbers)} is the median number of the list.')
print(calc_median(numbers))
