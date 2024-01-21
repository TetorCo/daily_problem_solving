def dayOfProgrammer(year):
    # Write your code here

    if year <= 1917:
        if year % 4 == 0:
            result = "12.09." + str(year)
            return result
        else:
            result = "13.09." + str(year)
            return result
    elif year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            result = "12.09." + str(year)
            return result
        else:
            result = "13.09." + str(year)
            return result
    else: ## year == 1918
        return "26.09.1918"