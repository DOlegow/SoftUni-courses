symbols_1 = input()
symbols_2 = input()
result_symbols = ''
result_symbols_1 = symbols_1

for i in range(len(symbols_1)):
    result_symbols = symbols_2[:i+1] + symbols_1[(i+1):]
    if result_symbols != result_symbols_1:
        print(result_symbols)
    result_symbols_1 = result_symbols

