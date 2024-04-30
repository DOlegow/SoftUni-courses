n = int(input())
count_of_positives = 0
sum_of_negatives = 0
positives = []
negatives = []

for i in range(n):
    number = int(input())
    if number >= 0:

        positives.append(number)
    elif number < 0:

        negatives.append(number)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')
