def process_numbers(data):
    try:
        nums = list(map(int, data.split()))
    except ValueError:
        return "Invalid"

    if len(nums) > 10 or  len(nums) <= 1:
        return "Invalid"

    for i in nums:
        if i > 10 or i < 0:
            return "Invalid"

    nums.sort()

    if nums[0] == 0:
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[0] = nums[i]
                nums[i] = 0
                break

    return "".join(map(str, nums))


value = input()
output = process_numbers(value)
print(output)
