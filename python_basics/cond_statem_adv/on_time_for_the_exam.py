# read user data

exam_hour = int(input())
exam_min = int(input())
arriving_hour = int(input())
arriving_min = int(input())

# logic

if exam_hour < 24 and exam_min < 60 and arriving_hour < 24 and arriving_min < 60:
    exam_time_in_min = exam_hour * 60 + exam_min
    arriving_time_in_min = arriving_hour * 60 + arriving_min


# output
if exam_hour < 24 and exam_min < 60 and arriving_hour < 24 and arriving_min < 60:
    if arriving_time_in_min > exam_time_in_min:
        print("Late")
    if exam_time_in_min >= arriving_time_in_min  and arriving_time_in_min >= (exam_time_in_min-30):
        print("On time")
    if arriving_time_in_min < (exam_time_in_min-30):
        print("Early")
    if exam_time_in_min > arriving_time_in_min > (exam_time_in_min-60):
        print(f'{exam_time_in_min - arriving_time_in_min}  minutes before the start')
    if arriving_time_in_min <= exam_time_in_min-60:
        hh = int((exam_time_in_min - arriving_time_in_min)/60)
        mm = (exam_time_in_min - arriving_time_in_min) % 60
        print(f'{hh}:{mm:02d} hours before the start')
    if exam_time_in_min < arriving_time_in_min < exam_time_in_min + 60:
        print(f'{arriving_time_in_min - exam_time_in_min} minutes after the start')
    if arriving_time_in_min >= exam_time_in_min + 60:
        hh = int((arriving_time_in_min - exam_time_in_min)/60)
        mm = (arriving_time_in_min - exam_time_in_min) % 60
        print(f'{hh}:{mm:02d} hours after the start')
