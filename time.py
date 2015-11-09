def get_second_from_timestamp(timestamp):
    '''
    @timestamp: in seconds, not millisecond (Epoch uses millisecond)
    '''
    time_format = '%M:%S'

    # get only minute:second
    time_in_minutes = datetime.datetime.fromtimestamp(
        timestamp).strftime(time_format)
    logging.info('minute: [%r]' % time_in_minutes)

    time = datetime.datetime.strptime(time_in_minutes, time_format)
    second = datetime.timedelta(
        hours=time.hour,
        minutes=time.minute,
        seconds=time.second).total_seconds()

    logging.info('second: [%r]' % second)
    return second


def get_remaining_second_to_next_hour(timestamp):
    '''
    @timestamp: in seconds, not millisecond (Epoch uses millisecond)
    '''
    second = get_second_from_timestamp(timestamp)
    return 3600 - second
