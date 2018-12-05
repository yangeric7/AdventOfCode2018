import parse
import datetime
import numpy as np

action_pattern = '''[{time}] {action}\n'''
guard_pattern = '''Guard #{id:d} begins shift'''
guard_info = {}

def part1(ordered_actions):
    current_guard = None
    start_time = None

    for current_time, action in ordered_actions:
        if action == 'wakes up':
            time_slept = int((current_time - start_time)/datetime.timedelta(minutes=1))
            guard_info[current_guard]['total_slept'] += time_slept
            indicies = range(start_time.minute,start_time.minute + time_slept)
            array_slice = np.take(guard_info[current_guard]['minute_asleep_count'], indicies, mode='wrap')
            array_slice += 1
            guard_info[current_guard]['minute_asleep_count'][start_time.minute:start_time.minute + time_slept] = array_slice
        elif action == 'falls asleep':
            start_time = current_time
        else:
            a = parse.parse(guard_pattern, action)
            current_guard = a['id']
            if current_guard not in guard_info:
                guard_info[current_guard] = {}
                guard_info[current_guard]['total_slept'] = 0
                guard_info[current_guard]['minute_asleep_count'] = np.zeros(60)

    longest_total_slept = -1
    longest_slept_guard = None
    longest_slept_minute = None

    for guard, info in guard_info.items():
        if info['total_slept'] > longest_total_slept:
            longest_total_slept = info['total_slept']
            longest_slept_guard = guard
            longest_slept_minute = np.argmax(info['minute_asleep_count'])

    return longest_slept_guard * longest_slept_minute

def part2():
    most_frequent_minute = None
    most_frequent_guard = None
    most_frequent = -1
    for guard, info in guard_info.items():
        guard_most_frequent = np.max(info['minute_asleep_count'])
        guard_most_frequent_minute = np.argmax(info['minute_asleep_count'])
        if guard_most_frequent > most_frequent:
            most_frequent = guard_most_frequent
            most_frequent_guard = guard
            most_frequent_minute = guard_most_frequent_minute
    print(most_frequent_guard, most_frequent_minute, most_frequent)
    return most_frequent_guard * most_frequent_minute

def main():
    action_list = []
    for action in open('input.txt'):
        a = parse.parse(action_pattern, action)
        time = datetime.datetime.strptime(a['time'], '%Y-%m-%d %H:%M')
        action_list.append((time, a['action']))
    
    ordered_actions = sorted(action_list)
    

    print('Part 1 Answer: ' + str(part1(ordered_actions)))
    print('Part 2 Answer: ' + str(part2()))

if __name__ == '__main__':
    main()