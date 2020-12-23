cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']

def pleaseConformOnePass(caps):
    if len(caps) == 0:
        return
    caps = caps + [caps[0]]
    start = 1
    for i in range(1, len(caps)):
        if caps[i] != caps[i - 1]:
            if caps[i] != caps[0]:
                start = i
            elif start == i - 1:
                print('Person in position', start, 'flip your cap!')
            else:
                print('People in positions: ', start,' through', i-1, 'flip your caps!')


if __name__ == '__main__':
    pleaseConformOnePass(cap1)
    pleaseConformOnePass(cap2)
