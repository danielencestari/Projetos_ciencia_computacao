def study_schedule(permanence_period, target_time):
    try:
        contador = 0
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                contador += 1
        return contador
    except TypeError:
        return None
