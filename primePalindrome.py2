#Define Necessary Tools
def isPalindrome(number):
    for i in range(0,(len(number)/2)+1): #Only functions if Passed a String Type
        if number[i] != number[-(i+1)]:
            return False
    return True

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

#Start Solution
maxNumber = 1000 #So max can easily for future possible use.
while True:
    if isPalindrome(str(maxNumber)):
        if isPrime(maxNumber):
            solution = maxNumber
            break
    maxNumber -= 1
if solution:
    print(solution)
else:
    print("No Solution Found")