def hour_plus_minute(hours=71):
    hour = int(hours / 60)
    minute = (hours / 60) - hour
    minute = int((minute * 60) + 0.1)
    plural_h = "hour" if hour == 1 else "hours"
    plural_m = "minute" if minute == 1 else "minutes"
    print(f'{hours} will become "{hour} {plural_h}, {minute} {plural_m}"')
