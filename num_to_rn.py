numeral_input = input("Enter the Roman Numeral: ")

def roman_to_int(numeral):
    final_value = 0
    
    #edge cases
    if "CM" in numeral:
        final_value += 900
        numeral = numeral.replace("CM", " ") #replacing with empty space
    if "CD" in numeral:
        final_value += 400
        numeral = numeral.replace("CD", " ")
    if "XC" in numeral:
        final_value += 90
        numeral = numeral.replace("XC", " ")
    if "XL" in numeral:
        final_value += 40
        numeral = numeral.replace("XL", " ")
    if "IX" in numeral:
        final_value += 9
        numeral = numeral.replace("IX", " ")
    if "IV" in numeral:
        final_value += 4
        numeral = numeral.replace("IV", " ")
    
    for i in range(len(numeral)):
        if numeral[i] == 'M':
            final_value += 1000
        elif numeral[i] == 'D':
            final_value += 500
        elif numeral[i] == 'C':
            final_value += 100
        elif numeral[i] == 'L':
            final_value += 50
        elif numeral[i] == 'X':
            final_value += 10
        elif numeral[i] == 'V':
            final_value += 5
        elif numeral[i] == 'I':
            final_value += 1
            
    print("Translation: " + str(final_value))

if __name__ == "__main__" :
        roman_to_int(numeral_input)