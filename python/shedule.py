"""
Can we find a time for meeting in our schedule?
"""

me = [
    '12:00 - 13:00',
    '13:00 - 13:30',
    '16:00 - 16:30',
    '16:40 - 17:20',
    '17:50 - 18:00',
    '18:30 - 19:30',
]

you = [
    '09:00 - 10:00',
    '11:20 - 12:10',
    '14:00 - 15:00',
    '16:30 - 17:00',
    '17:00 - 17:20',
    '18:00 - 19:00',
]

duration = 20

work_time = '05:00 - 21:00'


def item_validation(period: str) -> bool:
    if len(period) != 13:
        return False
    if period[2] != ':' and period[5:8] != ' - '  and period[10] != ':':
        return False
    try:
        a = int(period[:2]) + int(period[3:5]) + int(period[8:10]) + int(period[11:13])
    except ValueError:
        return False
    return True


def parse_item(period: str) -> tuple:
    if not item_validation(period):
        raise ValueError(f'The period string {period} is incorrect')
    start = (int(period[:2]) - int(work_time[:2])) * 60 + (
            int(period[3:5]) - int(work_time[3:5])
    )
    stop = (int(period[8:10]) - int(work_time[:2])) * 60 + int(period[11:13]) - int(work_time[3:5])
    return start, stop


def is_available(schedule: list, item: tuple) -> bool:
    if item <= parse_item(schedule[0]) and item[1] <= parse_item(schedule[0])[1]:
        return True
    for i in range(0, len(schedule) - 1):
        if item[0] >= parse_item(schedule[i])[1] and item[1] <= parse_item(schedule[i + 1])[0]:
            return True
    if item[0] >= parse_item(schedule[-1])[1] and item[1] <= parse_item(work_time)[1]:
        return True
    return False


def all_possible(schedule1, schedule2):
    all_times = iter(
        [(start, start + duration) for start in range(0, parse_item(work_time)[1], 10)])
    for time in all_times:
        if is_available(schedule1, time) and is_available(schedule2, time):
            yield time


if __name__ == '__main__':
    for item in all_possible(me, you):
        print(item)