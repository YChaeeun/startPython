
def ispalindrome(listString) :

    start = 0
    end = len(listString)-1

    while start < end :
        if listString[start].isalpha() == False :
            start += 1
        if listString[end].isalpha() == False :
            end -= 1

        if listString[start].lower() != listString[end].lower() :
            return False
        else :
            start += 1
            end -= 1

    return True

listString = input('Enter String :')

print(ispalindrome(listString))