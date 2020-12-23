def run_length_encoding(s : str):
    result = ''
    i = 0
    while  i < len(s):
        counter = 1
        while i + 1 < len(s) and s[i] == s[i  + 1]:
            counter += 1
            i += 1
        result += str(counter) + s[i]
        i += 1
    return result

def run_length_decoding(s : str):
    result = ''
    i = 0
    while i < len(s):
        start = i
        while i < len(s) and s[i].isnumeric():
            i += 1
        num = int(s[start:i])
        result += s[i] * num
        i += 1
    return result

if __name__ == '__main__':
    s = 'BWWWWWBWWWW'
    encoding = run_length_encoding(s)
    decoding = run_length_decoding(encoding)
    print(s == decoding)

