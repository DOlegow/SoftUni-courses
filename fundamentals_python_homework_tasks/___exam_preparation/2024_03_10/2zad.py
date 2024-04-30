import re


def process_barcode(barcode):
    # Check if the barcode matches the pattern
    if not re.match ( r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+', barcode ):
        print ( "Invalid barcode" )
        return

    # Extract digits from the barcode
    digits = ''.join ( filter ( str.isdigit, barcode ) )

    # Determine the product group
    product_group = digits if digits else "00"

    print ( f"Product group: {product_group}" )


# Read the number of barcodes
n = int ( input () )

# Process each barcode
for _ in range ( n ):
    barcode = input ().strip ()
    process_barcode ( barcode )
