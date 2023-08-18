# Given a clock time in hh:mm format, determine, to the nearest degree,
# the angle between the hour and the minute hands.

# Bonus: When, during the course of a day, will the angle be zero?

# Minute hand:

# It moves 360° in 60 minutes.
# So, it moves 6° per minute.

# Hour hand:

# It moves 360° in 12 hours.
# So, it moves 30° per hour or 0.5° per minute.
# Now, let's compute the angles made by the minute and hour hands with respect to 12:00 position.

# Given hh:mm:

# Angle made by minute hand = 6 * minutes
# Angle made by hour hand = 0.5 * (60 * hours + minutes)


# Bonus answer: The relative speed between the minute hand and the hour hand
# (how fast the minute hand is catching up) is the difference between their speeds:

# Relative speed = 6° - 0.5° = 5.5° per minute.

# Now, if you consider the clock at 12:00 (both hands at the top), the minute hand will have to move 360 degrees
# plus however much the hour hand has moved in the time it took for the minute hand to catch up.

# If t  is the time it takes for the minute hand to overlap the hour hand, then: The distance covered by the minute hand =
# 360° + (0.5° * t) The distance covered by the hour hand = 0.5° * t

# Since the minute hand moves at 6° per minute:

# 6t = 360 + 0.5t
# 5.5t = 360
# t = 360 / 5.5 = 65.45 (65 5/11) minutes


def clock_angle(hh, mm):
    minute_angle = 6 * mm
    hour_angle = 0.5 * (60 * hh + mm)

    # Calculate the absolute difference between the two angles
    angle = abs(minute_angle - hour_angle)

    # Since the maximum angle between them can be 180 degrees,
    # if it's greater than that, subtract from 360 to get the smaller angle
    return min(angle, 360 - angle)


def over_times():
    overlap_minutes = 65 + 5 / 11

    current_time_minutes = 0

    overlaps = []

    while current_time_minutes < 12 * 60:
        hh = int(current_time_minutes / 60)
        mm = current_time_minutes % 60
        # Append the formatted time
        overlaps.append(
            f"{hh:02d}:{int(mm):02d} and {int((mm % 1) * 60)} seconds")

        current_time_minutes += overlap_minutes  # Move to next overlap time

    return overlaps


if __name__ == "__main__":
    time = "02:30"
    hh, mm = map(int, time.split(":"))
    print(clock_angle(hh, mm))  # Should print 105.0 for 02:30

    overlaps = over_times()

    for time in overlaps:
        print(time)
