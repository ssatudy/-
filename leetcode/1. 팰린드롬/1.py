def func(s):
    s = s.lower()             # 일단 소문자화
    alnum = []                # 새로운 리스트를 만들어 준다.
    for i in s:               # 받은 문자열을 순회해준다. 이때 공백도 포함이 된다
        if i.isalnum():       # 문자열이 알파벳이거나 숫자인경우에
            alnum.append(i)   # 새로만든 리스트에 저장
    if alnum == alnum[::-1]:  # 리스트가 거꾸로해도 똑같은 경우
        return True
    else:
        return False



print(func('a@b :b a')) # True
print(func('won'))      # False
print(func('A man, a plan, a canal: Panama')) # True