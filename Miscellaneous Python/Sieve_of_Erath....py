def prime_checker(num):
    num_to_check = []
    for each_num_to_check in range(2, int(num ** 0.5) + 1):
        num_to_check.append(each_num_to_check)

    within_limit = True
    marked_nums = []
    prime_nums = []

    for each_num in num_to_check:
        if within_limit:
            for each_num_multiple in range(2, num + 1):
                multiple_limit = each_num_multiple * each_num
                if multiple_limit > num:
                    break

                if multiple_limit not in marked_nums:
                    marked_nums.append(multiple_limit)

    for each_prime in range(2, num + 1):
        if each_prime not in marked_nums:
            prime_nums.append(each_prime)

    return prime_nums



user_input = int(input("Put in the number that you wanna have prime number with: "))
print(prime_checker(user_input))


