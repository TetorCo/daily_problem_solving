def timeInWords(h, m):
    # Write your code here
    hours = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    minutes = ['', "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    

    def get_minute(minute):
        if minute == 1:
            return 'one minute'
        elif 1 < minute < 15 or 15 < minute <= 20:
            return f'{minutes[minute]} minutes'
        elif minute == 15:
            return 'quarter'
        elif minute == 30:
            return 'half'
        else:
            return f'{minutes[20]} {minutes[minute % 20]} minutes'

    if m == 0:
        return f"{hours[h]} o' clock"
    elif 0 < m <= 30:
        return f"{get_minute(m)} past {hours[h]}"
    elif 30 < m < 60:
        return f"{get_minute(60 - m)} to {hours[h + 1]}"
    
if __name__ == "__main__":
    print(timeInWords(6, 35))