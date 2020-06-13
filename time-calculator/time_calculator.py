def add_time(start, duration):
    # separate the time from the period
    old_date = start.split(' ')
    # separate the hours from the minutes
    old_time = old_date[0].split(':')
    duration_time = duration.split(':')

    # simple convention: use `h` and `m` variables to handle integers
    old_h = int(old_time[0])
    old_m = int(old_time[1])
    duration_h = int(duration_time[0])
    duration_m = int(duration_time[1])

    # add up the hour and minutes
    new_h = old_h + duration_h
    new_m = old_m + duration_m
    # round minutes
    if new_m >= 60:
        new_m = new_m % 60
        new_h += 1

    # round hours
    hours = str(new_h % 12)
    # zero-pad the minutes
    minutes = str(new_m).rjust(2, '0')

    # for the period switch the current string if the hours describe half a day past 11.59
    # half, three halves, five halves
    meridian = old_date[1]
    if new_h // 12 % 2 != 0:
        if meridian == 'AM':
            meridian = 'PM'
        else:
            meridian = 'AM'

    new_time = f'{hours}:{minutes} {meridian}'

    return new_time
