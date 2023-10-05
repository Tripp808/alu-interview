#!/usr/bin/python3

def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    :param walls: A list of non-negative integers representing wall heights.
    :return: Integer indicating the total amount of rainwater retained.
    """

    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if walls[left] <= walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                water += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                water += right_max - walls[right]
            right -= 1

    return water

# Test cases
if __name__ == "__main__":
    walls1 = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls1))  # Output: 6

    walls2 = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls2))  # Output: 6
