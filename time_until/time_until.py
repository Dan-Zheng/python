#!usr/bin/env python

from datetime import datetime

def main():
    now = datetime.now()

    current_minute = str(now.minute)
    if len(current_minute) < 2:
        current_minute = '0' + current_minute

    print 'The current time is: ' + str(now.hour) + ':' + current_minute  + '.'
    input_time = raw_input('Enter the time: (hour, minute)\n')

    if ',' in input_time:
        end_time = input_time.split(',')
        end_minute = int(end_time.pop())
        end_hour = int(end_time.pop())
    elif ':' in input_time:
        end_time = input_time.split(':')
        end_minute = int(end_time.pop())
        end_hour = int(end_time.pop())
    elif ' ' in input_time:
        end_time = input_time.split(' ')
        end_minute = int(end_time.pop())
        end_hour = int(end_time.pop())
    elif ';' in input_time:
        end_time = input_time.split(';')
        end_minute = int(end_time.pop())
        end_hour = int(end_time.pop())
    else:
        end_hour = int(input_time)
        end_minute = 0

    end_total_minutes = end_hour * 60 + end_minute
    now_total_minutes = now.hour * 60 + now.minute

    if end_total_minutes < now_total_minutes:
        final_total_minutes = 1440 - now_total_minutes + end_total_minutes
    else:
        final_total_minutes = end_total_minutes - now_total_minutes

    final_minute = str(final_total_minutes % 60)
    if len(final_minute) < 2:
        final_minute = '0' + final_minute
    final_hour = str(final_total_minutes / 60)

    print 'You have ' + final_hour + ':' + final_minute + '.'

if __name__ == '__main__':
    main()
