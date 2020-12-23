sched3 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2),(7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),(8.0, 10.0, 1), (9.0, 12.0, 2),(9.5, 10.0, 4), (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7)]

def bestTimeToPartySmart(schedule):
    # Convert schedule to list of start times and end times marked as such
    times = []
    for c in schedule:
        times.append((c[0], 'start', c[2]))
        times.append((c[1], 'end' , c[2]))

    # Sort the list of times.
    # Each time is a start or end time of a celebrity sighting.
    sortlist(times)
    ##    print times

    maxcount, time, max_score = chooseTime(times)

    # Output best time to party
    print('Best time to attend the party is at', time, \
          'o\'clock', ':', maxcount, 'celebrities will be attending!', 'overall score:', max_score)


# Sort the elements of tlist in ascending order
# Sorting is based on the value of the element tuple (both items!)
# The original code had a bug in that it did not look at the second
# item of each tuple and ensure that (x, 'end') of one interval
# is sorted before (x, 'start') of a different tuple.
def sortlist(tlist):
    for index in range(len(tlist) - 1):
        ismall = index
        for i in range(index, len(tlist)):
            # Sort based on first item of tuple
            if tlist[ismall][0] > tlist[i][0] or \
                    (tlist[ismall][0] == tlist[i][0] and \
                     tlist[ismall][1] > tlist[i][1]):
                ismall = i
        # Swap the positions of the elements at index and ismall indices
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]

    return


def chooseTime(times):
    rcount = 0
    maxcount = 0
    time = 0
    score = 0
    max_score = 0
    # Range through the times computing a running count of celebrities
    for t in times:
        if t[1] == 'start':
            rcount = rcount + 1
            score += t[2]
        elif t[1] == 'end':
            rcount = rcount - 1
            score -= t[2]
        if score > max_score:
           max_score = score
           maxcount = rcount
           time = t[0]

    return maxcount, time,  max_score


if __name__ == '__main__':
    bestTimeToPartySmart(sched3)
