from datetime import datetime


def estimate_date(input_date):
    # Convert input date string to datetime object
    input_date = datetime.strptime ( input_date, '%Y-%m-%d' )

    # Reference date (2018-08-26)
    reference_date = datetime ( 2018, 8, 26 )

    # Current date
    current_date = datetime ( 2018, 8, 25 )

    # Calculate the difference in days
    delta = input_date - current_date

    # Check if the input date has passed
    if delta.days < 0:
        print ( "Passed" )
    # Check if the input date is today
    elif delta.days == 1:
        print ( "Today date" )
    # Otherwise, print the number of days remaining
    else:
        print ( f"{delta.days} days left" )


# Example usage
input_date = input()  # You can change the date here
estimate_date ( input_date )
