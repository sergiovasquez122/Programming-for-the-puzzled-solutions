def palindrome_checker(s : str):
    if len(s) == 0 or len(s) == 1:
        return True
    return s[0].lower() == s[-1].lower() and palindrome_checker(s[1:len(s) - 1])

if __name__ == '__main__':
    print(palindrome_checker('kayak'))
    print(palindrome_checker('racecar'))
    print(palindrome_checker('kayaK'))
    print(palindrome_checker(''))
    print(palindrome_checker('s'))
    print(palindrome_checker('not a palindrome'))