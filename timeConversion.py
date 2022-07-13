"""Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""

def timeConversion(s):
    if s[-2] == "A" and s[:2] == "12":
        result = "00" + s[2:-2]
    elif s[-2] == "P" and s[:2] != "12":
        result = str(int(s[:2]) + 12) + s[2:-2]
    else:
        result = s[:-2]
    
    return result

if __name__ == '__main__':
    print(timeConversion("07:05:45PM"))
    print(timeConversion("12:45:54PM"))
    print(timeConversion("06:05:45PM"))
    print(timeConversion("01:05:45AM"))