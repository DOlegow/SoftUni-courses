import re


def extract_numbers(input_text):
    # Define a regular expression pattern to match numbers
    pattern = r'\d+'

    # Use the findall method to extract all numbers from the input text
    numbers = re.findall ( pattern, input_text )

    # Join the extracted numbers into a single string separated by a space
    extracted_numbers = ' '.join ( numbers )

    return extracted_numbers


def main():
    input_lines = []

    # Receive strings on different lines until an empty line is entered
    while True:
        line = input ( "Enter a string (or press Enter to stop): " )
        if not line:
            break
        input_lines.append ( line )

    # Combine the input lines into a single string
    input_text = '\n'.join ( input_lines )

    # Extract numbers from the input text
    extracted_numbers = extract_numbers ( input_text )

    # Print the extracted numbers
    print ( "Extracted numbers:", extracted_numbers )


if __name__ == "__main__":
    main ()
