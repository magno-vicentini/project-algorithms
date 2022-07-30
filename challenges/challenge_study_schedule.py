def study_schedule(permanence_period, target_time):
    count_students = 0
    if(target_time is None):
        return None
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        if period[0] <= target_time <= period[1]:
            count_students += 1
    return count_students
