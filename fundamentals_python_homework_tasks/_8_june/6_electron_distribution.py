number_of_electrons = int(input())
position_of_a_shell = 0
electron_distribution = []
element = 0

while number_of_electrons >= 2 * position_of_a_shell ** 2:
    position_of_a_shell += 1
    element = 2 * position_of_a_shell ** 2
    electron_distribution.append(element)
    number_of_electrons -= element
if number_of_electrons > 0:
    electron_distribution.append(number_of_electrons)
print(electron_distribution)
