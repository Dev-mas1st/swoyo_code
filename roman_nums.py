def roman_numerals_to_int(roman_numerals):
    try:
        map_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(roman_numerals) - 1):
            if map_values[roman_numerals[i]] < map_values[roman_numerals[i+1]]:
                result -= map_values[roman_numerals[i]]
            else:
                result += map_values[roman_numerals[i]]
        return result + map_values[roman_numerals[-1]]
    except:
        return None