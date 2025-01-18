def minutes_002040 (time_instance):
    '''
    Funció que arrodoneix una instància temps per grups de 20 minuts (e.g. '01:02:31' -> '01:00'):

    Args:
        pren una instància de temps com a argument, en format string 'hh:mm:ss'.

    Returns:
        :obj:`str`: retorna la nova instància de temps en format 'hh:mm'
    '''
    hours = time_instance[:5].split(':')[0]
    minutes = int(time_instance[:5].split(':')[1])

    print(hours, minutes)

    if minutes < 20:
        minutes = '00'
    elif minutes < 40:
        minutes = '20'
    else:
        minutes = '40'

    time = hours + ':' + minutes
    return time

