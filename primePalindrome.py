def isPalindrome(number):
    for i in range(0,(len(number)/2)+1):
        if number[i] != number[-(i+1)]:
            return False
    return True
