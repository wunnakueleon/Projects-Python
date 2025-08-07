def longest_consecutive_length(nums):
    consecutive_list = []
    sorted_list = sorted(nums)

    consecutive_list.append(sorted_list[0])
    for each_num in range(1, len(nums)):
        if (sorted_list[each_num] - 1 == sorted_list[each_num - 1]) or (sorted_list[each_num] == sorted_list[each_num - 1]):
            consecutive_list.append(sorted_list[each_num])


    return consecutive_list



print(len(longest_consecutive_length([0, 1, 3, 2, 1, 90, 28, 19])))



