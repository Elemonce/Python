def overlapping_intervals(interval1, interval2):
    # Unpack bounds
    left1, right1 = interval1
    left2, right2 = interval2

    # Check if one of interval2's bounds fall inside interval1
    # condition1 = left1 <= right1 
    # condition2 = left2 <= right2
    # condition3 = left1 <= right2

    condition1 = left1 <= right2
    condition2 = left2 <= right1
    condition3 = left1 <= right1
    condition4 = left2 <= right2
    # return left1 <= left2 <= right1 or left1 <= right2 <= right1
    # return condition1 and condition2 and condition3
    return condition1 and condition2 and condition3 and condition4

print(overlapping_intervals((9, 9), (8, 9)))