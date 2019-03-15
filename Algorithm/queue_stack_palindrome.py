
# queue : First In First Out
# stack : Last In First Out 

# 회문찾기 : 앞에서부터 읽거나 뒤에서 부터 읽어도 똑같은 문자열, 특수문자 및 공백은 무시

def ispalindrome(listString) :
    qu = list()
    st = list()

    for char in listString :
        if char.isalpha() :   # 공백 및 특수문자는 무시
            qu.append(char.lower())  # 소문자
            st.append(char.lower())

    while qu :
        if qu.pop(0) != st.pop() :
            return False
    return True


listString = input('Enter string : ')

print(ispalindrome(listString))