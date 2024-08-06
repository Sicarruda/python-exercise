# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def timeConversion(s):
    if "A" in s:
        if s[0] == "1" and s[1] == "2":
            
            s = s.replace(s[0], "0", 1)
            s = s.replace(s[1], "0", 1)
    
    if "P" in s:
        
        if (s[0] != "1" or s[1] != "2"):

            hour_str = s[0] + s[1]
            convertion_hour = int(hour_str) + 12
            hour_str = str(convertion_hour)
           
            s = s.replace(s[0], hour_str[0], 1)
            s = s.replace(s[1], hour_str[1], 1)
            
    s = s.replace(s[8], "")
    s = s.replace(s[8], "")
    
    return s