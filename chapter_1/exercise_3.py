cap3 = ['F','F','B','H','B','F','B','B','B','F','H','F','F']

def pleaseConformOnePass(caps):
    if len(caps) == 0:
        return
    first_hat_seen = -1
    for i in range(len(caps)):
        if caps[i] == 'F' or caps[i] == 'B':
            first_hat_seen = i
            break
    if first_hat_seen == -1:
        return
    caps = caps + [caps[first_hat_seen]]
    start = -1
    for i in range(first_hat_seen + 1, len(caps)):
        if caps[i] != caps[i - 1]:
            if caps[i] != caps[first_hat_seen] and caps[i] == 'B':
                start = i
            elif start == i - 1 and caps[start] == 'B':
                print('Person in position', start, 'flip your cap!')
            elif caps[i - 1] == 'B':
                print('People in positions:', start,'through', i-1, 'flip your caps!')

if __name__ == '__main__':
    pleaseConformOnePass(cap3)
