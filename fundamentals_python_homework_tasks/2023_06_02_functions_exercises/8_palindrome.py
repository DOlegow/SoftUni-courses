def is_palindrome_str(numbers):

    for element in numbers:

        is_palindrome = element == element[::-1]

        print(is_palindrome)


positive_numbers = input().split(", ")
is_palindrome_str(positive_numbers)





