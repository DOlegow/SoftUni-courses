price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
price_rating_expensive_or_cheap = input()

sum_of_price_ratings = 0
sum_of_price_ratings_left = 0
sum_of_price_ratings_right = 0
right = []
left = []
position = "Left"

for i in range(entry_point):
    left.append(price_ratings[i])
for j in range(entry_point+1, len(price_ratings)):
    right.append(price_ratings[j])

if price_rating_expensive_or_cheap == "cheap":
    for element in left:
        if element < price_ratings[entry_point]:
            sum_of_price_ratings_left += element
    for element in right:
        if element < price_ratings[entry_point]:
            sum_of_price_ratings_right += element

elif price_rating_expensive_or_cheap == "expensive":
    for el in left:
        if el >= price_ratings[entry_point]:
            sum_of_price_ratings_left += el
    for el in right:
        if el >= price_ratings[entry_point]:
            sum_of_price_ratings_right += el

if sum_of_price_ratings_left > sum_of_price_ratings_right:
    sum_of_price_ratings = sum_of_price_ratings_left
elif sum_of_price_ratings_right > sum_of_price_ratings_left:
    sum_of_price_ratings = sum_of_price_ratings_right
    position = "Right"
else:
    sum_of_price_ratings = sum_of_price_ratings_left

print(f'{position} - {sum_of_price_ratings}')


