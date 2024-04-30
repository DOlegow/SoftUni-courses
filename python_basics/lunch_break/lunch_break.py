# read user input

import math
film_name = str(input())
episode_duration = int(input())
break_duration = int(input())

# logic

lunch = break_duration/8
rest = break_duration/4
time_left = break_duration - lunch - rest
if time_left >= episode_duration:
    print(f'You have enough time to watch {film_name} and left with {math.ceil(time_left-episode_duration)} minutes free time.')
if time_left < episode_duration:
    print(f"You don't have enough time to watch {film_name}, you need {math.ceil(episode_duration-time_left)} more minutes.")