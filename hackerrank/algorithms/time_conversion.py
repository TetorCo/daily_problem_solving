def timeConversion(s):
    # Write your code here
    s = "12:40:22AM"
    time_format = s[-2:]
    hour, mina, sec = s[:-2].split(':')
    
    if time_format == "AM" and int(hour) == 12:
        hour = '00'
    elif time_format == "AM" and int(hour) != 12:
        hour = str(int(hour) - 12)
    elif time_format == "PM" and int(hour) != 12:
        hour = str(int(hour) + 12)
    
    result = hour + ":" + mina + ":" + sec
    print(result)
    return result

if __name__ == '__main__':

    timeConversion("1111")