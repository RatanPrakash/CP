t = int(input())

for _ in range(t):
    time = input()

    hours, minutes = map(int, time.split(':'))

    if hours < 12:
        meridian = 'AM'
    else:
        meridian = 'PM'

    if hours == 0:
        hours = 12
    
    elif hours > 12:
        hours -= 12

    print(f'{hours:02d}:{minutes:02d} {meridian}')
