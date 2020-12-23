sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
         (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
sched3 = [(6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8),
          (9, 10), (11, 12), (11, 13), (11, 14)]

def best_time(schedule):
    max_celebs = 0
    time = 0
    for i in range(len(schedule)):
        start_time = schedule[i][0]
        counter = 0
        for j in range(len(schedule)):
            if start_time >= schedule[j][0] and start_time < schedule[j][1]:
                counter += 1
            if max_celebs < counter:
                max_celebs = counter
                time = start_time
    print('Best time to attend the party is at', time, \
          'o\'clock', ':', max_celebs, 'celebrities will be attending!')

if __name__ == '__main__':
    best_time(sched2)
    best_time(sched3)

