def get_modifier(stat):
    modifier = 0
    stat = int(stat)
    if stat == 0:
        modifier = -3
    elif tat >= 1 and int(stat) < 3:
        modifier = -2
    elif int(stat) >= 3 and int(stat) < 6:
        modifier = -1
    elif int(stat) >= 6 and int(stat) < 9:
        modifier = 0
    elif int(stat) >= 9 and int(stat) < 12:
        modifier = 1
    elif int(stat) >= 12 and int(stat) < 15:
        modifier = 2
    elif int(stat) >= 15:
        modifier = 3
    return modifier