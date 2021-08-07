def hour_plus_minute(hours=71):
    hour = int(hours / 60)
    minute = (hours / 60) - hour
    minute = int(minute * 60)
    print(f"{hours} will become \"{hour} hours, {minute} minutes\"")
