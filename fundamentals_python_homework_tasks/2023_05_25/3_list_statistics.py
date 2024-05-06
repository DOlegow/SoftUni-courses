n = int(input())
count_of_positives = 0
sum_of_negatives = 0
positives = []
negatives = []

for i in range(n):
    number = int(input())
    if number >= 0:
        count_of_positives += 1
        positives.append(number)
    elif number < 0:
        sum_of_negatives += number
        negatives.append(number)

print(positives)
print(negatives)
print(f'Count of positives: {count_of_positives}')
print(f'Sum of negatives: {sum_of_negatives}')

