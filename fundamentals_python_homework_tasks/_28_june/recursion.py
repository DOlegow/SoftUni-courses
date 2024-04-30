def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = nums[middle]

        if target == middle_element:
            return middle
        elif target < middle_element:
            right = middle - 1
        else:
            left = middle + 1


nums = [int(x) for x in input().split()]
target = int(input('Target number: '))
print(binary_search(nums, target))



# list_of_numbers = list(map(int, input().split()))
# searched_number = int(input())
# middle_number = len(list_of_numbers) // 2
# while True:
#     if middle_number == searched_number:
#         break
#     middle_number = len(list_of_numbers) // 2
#     if searched_number < list_of_numbers[middle_number]:
#
# print(f'Searched number {searched_number} is on index {list_of_numbers[middle_number]} in list of numbers')