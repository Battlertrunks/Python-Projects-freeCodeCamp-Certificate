def add_time(start, duration, day = ''):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Format the time to be mutable in code
    # TODO: I want to refactor this
    splitTimes = start.split(':')
    startTimeNums = [int(splitTimes[0]), int(splitTimes[1].split(' ')[0])]
    timeOfDay = splitTimes[1].split(' ')[1]
    durationNum = [int(duration.split(':')[0]), int(duration.split(':')[1])]
    curDay = days.index(day.lower()) if day else -1
    daysPass = 0    

    # Calculate time passed with current time
    # TODO: I should refactor this
    for index in range(len(startTimeNums)-1, -1, -1):
        startTimeNums[index] += durationNum[index]

        # If minutes are going to an hour or more, add hour to current time
        if index == 1 and startTimeNums[index] > 59:
            startTimeNums[index] -= 60
            startTimeNums[index-1] += 1

        # If current time in addition with time passed is over 12 hours, update 'PM' or 'AM'.
        if index == 0 and startTimeNums[index] >= 12:
            if (startTimeNums[index] // 12) % 2 and timeOfDay == 'PM':
                timeOfDay = 'AM'
                daysPass += 1
            elif (startTimeNums[index] // 12) % 2  and timeOfDay == 'AM':
                timeOfDay = 'PM'

            # See if any days past and document them
            if startTimeNums[index] > 24:
                daysPass = round(startTimeNums[index] / 24)

            # Set proper 12-hour time
            startTimeNums[index] %= 12
            if startTimeNums[index] == 0:
                startTimeNums[index] = 12

        # Format the time back into a string and sets proper amount of digits
        if index == 0:
            startTimeNums[index] = f"{startTimeNums[index]:01d}"
        else:
            startTimeNums[index] = f"{startTimeNums[index]:02d}"

    # Join the hours, minutes, and AM/PM with the colon (:) in the middle
    time = ':'.join(startTimeNums) + f' {timeOfDay}'

    # Set day of week if enabled (is disabled if curDay is -1)
    if curDay >= 0:
        time += f', {days[(daysPass + curDay) % 7].capitalize()}'

    # Add the number of days that have passed, ex: (9 days later)
    if daysPass:
        if daysPass == 1:
            time += ' (next day)'
        else:
            time += f' ({daysPass} days later)'

    return str(time)
