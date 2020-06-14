def add_time(start, duration, day_of_week=None):
    time_start, time_period = start.split(" ")
    hours_start, minutes_start = time_start.split(":")
    hours_duration, minutes_duration = duration.split(":")

    hours = int(hours_start) + int(hours_duration)
    minutes = int(minutes_start) + int(minutes_duration)

    hours_excess = minutes // 60
    minutes = minutes % 60
    hours += hours_excess

    half_days_excess = hours // 12
    hours = hours % 12
    days_excess = half_days_excess // 2

    if time_period == 'PM' and not half_days_excess % 2 == 0:
        days_excess += 1
    # show 12 instead of 0 hours
    if hours == 0:
        hours = 12

    hours_end = str(hours)
    minutes_end = str(minutes).rjust(2, "0")

    period = time_period
    if not half_days_excess % 2 == 0:
        if period == 'AM':
            period = 'PM'
        else:
            period = 'AM'

    end = hours_end + ":" + minutes_end + " " + period

    if day_of_week:
        days_of_week = ['monday', 'tuesday', 'wednesday',
                        'thursday', 'friday', 'saturday', 'sunday']

        day_start = day_of_week.lower()
        day_start_index = days_of_week.index(day_start)
        day_end_index = (day_start_index + days_excess) % len(days_of_week)
        day_end = days_of_week[day_end_index]

        end += ", " + day_end[0].upper() + day_end[1:]

    if days_excess == 1:
        end += " (next day)"
    if days_excess > 1:
        end += " (" + str(days_excess) + " days later)"

    return end
